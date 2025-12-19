from typing import Optional, List, Dict, Any
import re
from datetime import datetime


def count_words(text: str) -> int:
    """Count words in text"""
    if not text:
        return 0
    return len(text.split())


def count_arabic_words(text: str) -> int:
    """Count Arabic words in text"""
    if not text:
        return 0
    # Remove English words and count Arabic words
    arabic_text = re.sub(r'[a-zA-Z]+', '', text)
    return len(arabic_text.split())


def sanitize_filename(filename: str) -> str:
    """Sanitize filename"""
    # Remove special characters
    filename = re.sub(r'[^\w\s\-.]', '', filename)
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    return filename


def format_citation_apa(reference: Dict[str, Any]) -> str:
    """Format reference in APA style"""
    authors = reference.get('authors', [])
    year = reference.get('year', 'n.d.')
    title = reference.get('title', '')
    
    # Format authors
    if len(authors) == 0:
        author_str = "Unknown"
    elif len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        author_str = f"{authors[0]} & {authors[1]}"
    else:
        author_str = f"{authors[0]} et al."
    
    citation = f"{author_str} ({year}). {title}."
    
    # Add journal/book info
    if reference.get('journal_name'):
        citation += f" {reference['journal_name']}"
        if reference.get('volume'):
            citation += f", {reference['volume']}"
        if reference.get('issue'):
            citation += f"({reference['issue']})"
        if reference.get('pages'):
            citation += f", {reference['pages']}"
    
    if reference.get('publisher'):
        citation += f" {reference['publisher']}"
    
    if reference.get('doi'):
        citation += f" https://doi.org/{reference['doi']}"
    elif reference.get('url'):
        citation += f" {reference['url']}"
    
    return citation


def format_citation_mla(reference: Dict[str, Any]) -> str:
    """Format reference in MLA style"""
    authors = reference.get('authors', [])
    title = reference.get('title', '')
    
    # Format authors
    if len(authors) == 0:
        author_str = "Unknown"
    elif len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        author_str = f"{authors[0]}, and {authors[1]}"
    else:
        author_str = f"{authors[0]}, et al."
    
    citation = f"{author_str}. \"{title}.\""
    
    if reference.get('journal_name'):
        citation += f" {reference['journal_name']}"
    
    if reference.get('volume'):
        citation += f" vol. {reference['volume']}"
    
    if reference.get('issue'):
        citation += f", no. {reference['issue']}"
    
    if reference.get('year'):
        citation += f", {reference['year']}"
    
    if reference.get('pages'):
        citation += f", pp. {reference['pages']}"
    
    if reference.get('url'):
        citation += f". {reference['url']}"
    
    return citation


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
    """Extract keywords from text (simple implementation)"""
    if not text:
        return []
    
    # Remove special characters and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words
    words = text.split()
    
    # Count word frequency
    word_freq = {}
    for word in words:
        if len(word) > 3:  # Ignore short words
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:max_keywords]]


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format datetime to string"""
    if not dt:
        return ""
    return dt.strftime(format_str)
