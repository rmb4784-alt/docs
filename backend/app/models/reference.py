from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class ReferenceType(str, enum.Enum):
    """Reference type enum"""
    BOOK = "book"
    JOURNAL = "journal"
    ARTICLE = "article"
    WEBSITE = "website"
    THESIS = "thesis"
    CONFERENCE = "conference"
    REPORT = "report"
    OTHER = "other"


class Reference(Base):
    """Reference model"""
    __tablename__ = "references"
    
    id = Column(Integer, primary_key=True, index=True)
    research_id = Column(Integer, ForeignKey("researches.id"), nullable=False)
    
    reference_type = Column(Enum(ReferenceType), nullable=False)
    
    # Common fields
    title = Column(String(500), nullable=False)
    authors = Column(JSON)  # List of authors
    year = Column(String(4))
    
    # Book specific
    publisher = Column(String(255))
    isbn = Column(String(20))
    edition = Column(String(50))
    
    # Journal/Article specific
    journal_name = Column(String(255))
    volume = Column(String(20))
    issue = Column(String(20))
    pages = Column(String(50))
    doi = Column(String(100))
    
    # Website specific
    url = Column(String(1000))
    access_date = Column(DateTime(timezone=True))
    
    # Conference specific
    conference_name = Column(String(255))
    location = Column(String(255))
    
    # Additional
    abstract = Column(Text)
    notes = Column(Text)
    
    # Citation text (formatted)
    citation_text = Column(Text)
    
    # Order in reference list
    order = Column(Integer, default=0)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    research = relationship("Research", back_populates="references")
    
    def __repr__(self):
        return f"<Reference {self.title}>"
