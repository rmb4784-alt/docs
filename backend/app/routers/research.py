from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from app.database import get_db
from app.models.research import Research, ResearchSection, ResearchStatus, CitationStyle
from app.models.user import User
from app.routers.auth import get_current_user

router = APIRouter()


# Schemas
class ResearchCreate(BaseModel):
    title: str
    title_ar: Optional[str] = None
    abstract: Optional[str] = None
    abstract_ar: Optional[str] = None
    keywords: Optional[List[str]] = None
    field_of_study: Optional[str] = None
    research_type: Optional[str] = "paper"
    language: str = "ar"
    citation_style: CitationStyle = CitationStyle.APA


class ResearchUpdate(BaseModel):
    title: Optional[str] = None
    title_ar: Optional[str] = None
    abstract: Optional[str] = None
    abstract_ar: Optional[str] = None
    keywords: Optional[List[str]] = None
    field_of_study: Optional[str] = None
    research_type: Optional[str] = None
    language: Optional[str] = None
    citation_style: Optional[CitationStyle] = None
    status: Optional[ResearchStatus] = None


class ResearchResponse(BaseModel):
    id: int
    title: str
    title_ar: Optional[str]
    abstract: Optional[str]
    abstract_ar: Optional[str]
    keywords: Optional[List[str]]
    field_of_study: Optional[str]
    research_type: Optional[str]
    language: str
    citation_style: CitationStyle
    status: ResearchStatus
    word_count: int
    page_count: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True


class SectionCreate(BaseModel):
    title: str
    content: Optional[str] = None
    section_type: Optional[str] = None
    order: int = 0


class SectionUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    section_type: Optional[str] = None
    order: Optional[int] = None


class SectionResponse(BaseModel):
    id: int
    research_id: int
    title: str
    content: Optional[str]
    section_type: Optional[str]
    order: int
    word_count: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True


@router.post("/", response_model=ResearchResponse, status_code=status.HTTP_201_CREATED)
async def create_research(
    research_data: ResearchCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new research project"""
    
    research = Research(
        user_id=current_user.id,
        title=research_data.title,
        title_ar=research_data.title_ar,
        abstract=research_data.abstract,
        abstract_ar=research_data.abstract_ar,
        keywords=research_data.keywords or [],
        field_of_study=research_data.field_of_study,
        research_type=research_data.research_type,
        language=research_data.language,
        citation_style=research_data.citation_style,
        status=ResearchStatus.DRAFT
    )
    
    db.add(research)
    await db.commit()
    await db.refresh(research)
    
    return research


@router.get("/", response_model=List[ResearchResponse])
async def list_researches(
    status: Optional[ResearchStatus] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List user's research projects"""
    
    query = select(Research).where(Research.user_id == current_user.id)
    
    if status:
        query = query.where(Research.status == status)
    
    query = query.order_by(Research.updated_at.desc()).offset(skip).limit(limit)
    
    result = await db.execute(query)
    researches = result.scalars().all()
    
    return researches


@router.get("/{research_id}", response_model=ResearchResponse)
async def get_research(
    research_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific research project"""
    
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    return research


@router.put("/{research_id}", response_model=ResearchResponse)
async def update_research(
    research_id: int,
    research_data: ResearchUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update a research project"""
    
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    # Update fields
    for field, value in research_data.model_dump(exclude_unset=True).items():
        setattr(research, field, value)
    
    await db.commit()
    await db.refresh(research)
    
    return research


@router.delete("/{research_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_research(
    research_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a research project"""
    
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    await db.delete(research)
    await db.commit()


# Section endpoints
@router.post("/{research_id}/sections", response_model=SectionResponse, status_code=status.HTTP_201_CREATED)
async def create_section(
    research_id: int,
    section_data: SectionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new section in research"""
    
    # Verify research ownership
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    section = ResearchSection(
        research_id=research_id,
        title=section_data.title,
        content=section_data.content,
        section_type=section_data.section_type,
        order=section_data.order,
        word_count=len(section_data.content.split()) if section_data.content else 0
    )
    
    db.add(section)
    await db.commit()
    await db.refresh(section)
    
    return section


@router.get("/{research_id}/sections", response_model=List[SectionResponse])
async def list_sections(
    research_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all sections of a research"""
    
    # Verify research ownership
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    result = await db.execute(
        select(ResearchSection)
        .where(ResearchSection.research_id == research_id)
        .order_by(ResearchSection.order)
    )
    sections = result.scalars().all()
    
    return sections


@router.put("/{research_id}/sections/{section_id}", response_model=SectionResponse)
async def update_section(
    research_id: int,
    section_id: int,
    section_data: SectionUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update a section"""
    
    # Verify research ownership
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    result = await db.execute(
        select(ResearchSection).where(
            and_(
                ResearchSection.id == section_id,
                ResearchSection.research_id == research_id
            )
        )
    )
    section = result.scalar_one_or_none()
    
    if not section:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Section not found"
        )
    
    # Update fields
    for field, value in section_data.model_dump(exclude_unset=True).items():
        setattr(section, field, value)
    
    # Update word count if content changed
    if section_data.content:
        section.word_count = len(section_data.content.split())
    
    await db.commit()
    await db.refresh(section)
    
    return section


@router.delete("/{research_id}/sections/{section_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_section(
    research_id: int,
    section_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a section"""
    
    # Verify research ownership
    result = await db.execute(
        select(Research).where(
            and_(Research.id == research_id, Research.user_id == current_user.id)
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    result = await db.execute(
        select(ResearchSection).where(
            and_(
                ResearchSection.id == section_id,
                ResearchSection.research_id == research_id
            )
        )
    )
    section = result.scalar_one_or_none()
    
    if not section:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Section not found"
        )
    
    await db.delete(section)
    await db.commit()
