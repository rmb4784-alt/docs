from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class ResearchStatus(str, enum.Enum):
    """Research status enum"""
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    COMPLETED = "completed"
    PUBLISHED = "published"


class CitationStyle(str, enum.Enum):
    """Citation style enum"""
    APA = "apa"
    MLA = "mla"
    CHICAGO = "chicago"
    HARVARD = "harvard"
    IEEE = "ieee"


class Research(Base):
    """Research model"""
    __tablename__ = "researches"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    title = Column(String(500), nullable=False)
    title_ar = Column(String(500))  # Arabic title
    
    abstract = Column(Text)
    abstract_ar = Column(Text)  # Arabic abstract
    
    keywords = Column(JSON)  # List of keywords
    
    field_of_study = Column(String(255))
    research_type = Column(String(100))  # Thesis, Paper, Report, etc.
    
    language = Column(String(10), default="ar")  # ar, en
    citation_style = Column(Enum(CitationStyle), default=CitationStyle.APA)
    
    status = Column(Enum(ResearchStatus), default=ResearchStatus.DRAFT)
    
    word_count = Column(Integer, default=0)
    page_count = Column(Integer, default=0)
    
    metadata = Column(JSON)  # Additional metadata
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True))
    
    # Relationships
    user = relationship("User", back_populates="researches")
    sections = relationship("ResearchSection", back_populates="research", cascade="all, delete-orphan")
    references = relationship("Reference", back_populates="research", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Research {self.title}>"


class ResearchSection(Base):
    """Research section model"""
    __tablename__ = "research_sections"
    
    id = Column(Integer, primary_key=True, index=True)
    research_id = Column(Integer, ForeignKey("researches.id"), nullable=False)
    
    title = Column(String(500), nullable=False)
    content = Column(Text)
    
    section_type = Column(String(50))  # introduction, methodology, results, etc.
    order = Column(Integer, default=0)
    
    word_count = Column(Integer, default=0)
    
    ai_generated = Column(JSON)  # Track AI generation metadata
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    research = relationship("Research", back_populates="sections")
    
    def __repr__(self):
        return f"<ResearchSection {self.title}>"
