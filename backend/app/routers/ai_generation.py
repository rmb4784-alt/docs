from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from app.models.user import User
from app.routers.auth import get_current_user
from app.services.ai_service import ai_service

router = APIRouter()


# Schemas
class GenerateIntroductionRequest(BaseModel):
    title: str
    field_of_study: str
    language: str = "ar"
    provider: str = "openai"


class GenerateConclusionRequest(BaseModel):
    title: str
    content_summary: str
    language: str = "ar"
    provider: str = "openai"


class ImproveTextRequest(BaseModel):
    text: str
    language: str = "ar"
    provider: str = "openai"


class CheckGrammarRequest(BaseModel):
    text: str
    language: str = "ar"


class GenerateContentRequest(BaseModel):
    prompt: str
    section_type: Optional[str] = None
    language: str = "ar"
    provider: str = "openai"
    temperature: float = 0.7
    max_tokens: int = 2000


class AIResponse(BaseModel):
    generated_text: str
    provider: str
    language: str


class GrammarCheckResponse(BaseModel):
    original_text: str
    corrected_text: str
    language: str


@router.post("/generate/introduction", response_model=AIResponse)
async def generate_introduction(
    request: GenerateIntroductionRequest,
    current_user: User = Depends(get_current_user)
):
    """Generate research introduction using AI"""
    
    try:
        generated_text = await ai_service.generate_research_introduction(
            title=request.title,
            field_of_study=request.field_of_study,
            language=request.language,
            provider=request.provider
        )
        
        return {
            "generated_text": generated_text,
            "provider": request.provider,
            "language": request.language
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate introduction: {str(e)}"
        )


@router.post("/generate/conclusion", response_model=AIResponse)
async def generate_conclusion(
    request: GenerateConclusionRequest,
    current_user: User = Depends(get_current_user)
):
    """Generate research conclusion using AI"""
    
    try:
        generated_text = await ai_service.generate_research_conclusion(
            title=request.title,
            content_summary=request.content_summary,
            language=request.language,
            provider=request.provider
        )
        
        return {
            "generated_text": generated_text,
            "provider": request.provider,
            "language": request.language
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate conclusion: {str(e)}"
        )


@router.post("/improve", response_model=AIResponse)
async def improve_text(
    request: ImproveTextRequest,
    current_user: User = Depends(get_current_user)
):
    """Improve academic text using AI"""
    
    try:
        improved_text = await ai_service.improve_text(
            text=request.text,
            language=request.language,
            provider=request.provider
        )
        
        return {
            "generated_text": improved_text,
            "provider": request.provider,
            "language": request.language
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to improve text: {str(e)}"
        )


@router.post("/check-grammar", response_model=GrammarCheckResponse)
async def check_grammar(
    request: CheckGrammarRequest,
    current_user: User = Depends(get_current_user)
):
    """Check grammar and provide corrections"""
    
    try:
        result = await ai_service.check_grammar(
            text=request.text,
            language=request.language
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to check grammar: {str(e)}"
        )


@router.post("/generate/custom", response_model=AIResponse)
async def generate_custom_content(
    request: GenerateContentRequest,
    current_user: User = Depends(get_current_user)
):
    """Generate custom content using AI"""
    
    try:
        if request.language == "ar":
            system_message = "أنت مساعد أكاديمي متخصص في كتابة البحوث الجامعية باللغة العربية."
        else:
            system_message = "You are an academic assistant specialized in writing university research papers."
        
        if request.provider == "openai":
            generated_text = await ai_service.generate_with_openai(
                prompt=request.prompt,
                system_message=system_message,
                temperature=request.temperature,
                max_tokens=request.max_tokens
            )
        else:
            generated_text = await ai_service.generate_with_gemini(
                prompt=request.prompt,
                temperature=request.temperature
            )
        
        return {
            "generated_text": generated_text,
            "provider": request.provider,
            "language": request.language
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate content: {str(e)}"
        )


@router.post("/paraphrase", response_model=AIResponse)
async def paraphrase_text(
    request: ImproveTextRequest,
    current_user: User = Depends(get_current_user)
):
    """Paraphrase text using AI"""
    
    try:
        if request.language == "ar":
            system_message = "أنت مساعد متخصص في إعادة صياغة النصوص الأكاديمية."
            prompt = f"""أعد صياغة النص التالي بأسلوب أكاديمي مختلف مع الحفاظ على المعنى الأصلي:

{request.text}

استخدم مفردات وتراكيب مختلفة مع الحفاظ على الدقة الأكاديمية."""
        else:
            system_message = "You are an assistant specialized in paraphrasing academic texts."
            prompt = f"""Paraphrase the following text in a different academic style while maintaining the original meaning:

{request.text}

Use different vocabulary and structures while maintaining academic precision."""
        
        if request.provider == "openai":
            paraphrased_text = await ai_service.generate_with_openai(
                prompt=prompt,
                system_message=system_message,
                temperature=0.7
            )
        else:
            paraphrased_text = await ai_service.generate_with_gemini(
                prompt=prompt,
                temperature=0.7
            )
        
        return {
            "generated_text": paraphrased_text,
            "provider": request.provider,
            "language": request.language
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to paraphrase text: {str(e)}"
        )


@router.post("/summarize", response_model=AIResponse)
async def summarize_text(
    request: ImproveTextRequest,
    current_user: User = Depends(get_current_user)
):
    """Summarize text using AI"""
    
    try:
        if request.language == "ar":
            system_message = "أنت مساعد متخصص في تلخيص النصوص الأكاديمية."
            prompt = f"""قم بتلخيص النص التالي بشكل موجز ودقيق:

{request.text}

يجب أن يتضمن الملخص النقاط الرئيسية فقط."""
        else:
            system_message = "You are an assistant specialized in summarizing academic texts."
            prompt = f"""Summarize the following text concisely and accurately:

{request.text}

The summary should include only the main points."""
        
        if request.provider == "openai":
            summary = await ai_service.generate_with_openai(
                prompt=prompt,
                system_message=system_message,
                temperature=0.3
            )
        else:
            summary = await ai_service.generate_with_gemini(
                prompt=prompt,
                temperature=0.3
            )
        
        return {
            "generated_text": summary,
            "provider": request.provider,
            "language": request.language
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to summarize text: {str(e)}"
        )
