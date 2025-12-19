from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from app.database import get_db
from app.models.reference import Reference, ReferenceType
from app.models.research import Research
from app.models.user import User
from app.routers.auth import get_current_user
from app.utils.helpers import format_citation_apa, format_citation_mla

router = APIRouter()


# Schemas
class ReferenceCreate(BaseModel):
    research_id: int
    reference_type: ReferenceType
    title: str
    authors: List[str]
    year: Optional[str] = None
    publisher: Optional[str] = None
    isbn: Optional[str] = None
    edition: Optional[str] = None
    journal_name: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    conference_name: Optional[str] = None
    location: Optional[str] = None
    abstract: Optional[str] = None
    notes: Optional[str] = None
    order: int = 0


class ReferenceUpdate(BaseModel):
    reference_type: Optional[ReferenceType] = None
    title: Optional[str] = None
    authors: Optional[List[str]] = None
    year: Optional[str] = None
    publisher: Optional[str] = None
    isbn: Optional[str] = None
    edition: Optional[str] = None
    journal_name: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    conference_name: Optional[str] = None
    location: Optional[str] = None
    abstract: Optional[str] = None
    notes: Optional[str] = None
    order: Optional[int] = None


class ReferenceResponse(BaseModel):
    id: int
    research_id: int
    reference_type: ReferenceType
    title: str
    authors: List[str]
    year: Optional[str]
    publisher: Optional[str]
    isbn: Optional[str]
    edition: Optional[str]
    journal_name: Optional[str]
    volume: Optional[str]
    issue: Optional[str]
    pages: Optional[str]
    doi: Optional[str]
    url: Optional[str]
    conference_name: Optional[str]
    location: Optional[str]
    citation_text: Optional[str]
    order: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class FormatCitationRequest(BaseModel):
    reference: ReferenceCreate
    style: str = "apa"  # apa, mla, chicago, harvard


@router.post("/", response_model=ReferenceResponse, status_code=status.HTTP_201_CREATED)
async def create_reference(
    reference_data: ReferenceCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new reference"""
    
    # Verify research ownership
    result = await db.execute(
        select(Research).where(
            and_(
                Research.id == reference_data.research_id,
                Research.user_id == current_user.id
            )
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research not found"
        )
    
    # Format citation based on research citation style
    reference_dict = reference_data.model_dump()
    if research.citation_style.value == "apa":
        citation_text = format_citation_apa(reference_dict)
    elif research.citation_style.value == "mla":
        citation_text = format_citation_mla(reference_dict)
    else:
        citation_text = format_citation_apa(reference_dict)  # Default to APA
    
    reference = Reference(
        **reference_data.model_dump(),
        citation_text=citation_text
    )
    
    db.add(reference)
    await db.commit()
    await db.refresh(reference)
    
    return reference


@router.get("/research/{research_id}", response_model=List[ReferenceResponse])
async def list_references(
    research_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all references for a research"""
    
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
        select(Reference)
        .where(Reference.research_id == research_id)
        .order_by(Reference.order, Reference.created_at)
    )
    references = result.scalars().all()
    
    return references


@router.get("/{reference_id}", response_model=ReferenceResponse)
async def get_reference(
    reference_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get a specific reference"""
    
    result = await db.execute(select(Reference).where(Reference.id == reference_id))
    reference = result.scalar_one_or_none()
    
    if not reference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reference not found"
        )
    
    # Verify ownership through research
    result = await db.execute(
        select(Research).where(
            and_(
                Research.id == reference.research_id,
                Research.user_id == current_user.id
            )
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    
    return reference


@router.put("/{reference_id}", response_model=ReferenceResponse)
async def update_reference(
    reference_id: int,
    reference_data: ReferenceUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update a reference"""
    
    result = await db.execute(select(Reference).where(Reference.id == reference_id))
    reference = result.scalar_one_or_none()
    
    if not reference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reference not found"
        )
    
    # Verify ownership through research
    result = await db.execute(
        select(Research).where(
            and_(
                Research.id == reference.research_id,
                Research.user_id == current_user.id
            )
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    
    # Update fields
    for field, value in reference_data.model_dump(exclude_unset=True).items():
        setattr(reference, field, value)
    
    # Re-format citation
    reference_dict = {
        "reference_type": reference.reference_type.value,
        "title": reference.title,
        "authors": reference.authors,
        "year": reference.year,
        "publisher": reference.publisher,
        "journal_name": reference.journal_name,
        "volume": reference.volume,
        "issue": reference.issue,
        "pages": reference.pages,
        "doi": reference.doi,
        "url": reference.url,
    }
    
    if research.citation_style.value == "apa":
        reference.citation_text = format_citation_apa(reference_dict)
    elif research.citation_style.value == "mla":
        reference.citation_text = format_citation_mla(reference_dict)
    else:
        reference.citation_text = format_citation_apa(reference_dict)
    
    await db.commit()
    await db.refresh(reference)
    
    return reference


@router.delete("/{reference_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reference(
    reference_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete a reference"""
    
    result = await db.execute(select(Reference).where(Reference.id == reference_id))
    reference = result.scalar_one_or_none()
    
    if not reference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reference not found"
        )
    
    # Verify ownership through research
    result = await db.execute(
        select(Research).where(
            and_(
                Research.id == reference.research_id,
                Research.user_id == current_user.id
            )
        )
    )
    research = result.scalar_one_or_none()
    
    if not research:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    
    await db.delete(reference)
    await db.commit()


@router.post("/format-citation", response_model=dict)
async def format_citation(
    request: FormatCitationRequest,
    current_user: User = Depends(get_current_user)
):
    """Format a citation in specified style"""
    
    reference_dict = request.reference.model_dump()
    
    if request.style == "apa":
        citation_text = format_citation_apa(reference_dict)
    elif request.style == "mla":
        citation_text = format_citation_mla(reference_dict)
    else:
        citation_text = format_citation_apa(reference_dict)  # Default to APA
    
    return {
        "citation_text": citation_text,
        "style": request.style
    }
