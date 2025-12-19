from typing import Optional, Dict, List
import openai
from openai import AsyncOpenAI
import google.generativeai as genai
from app.config import settings


class AIService:
    """AI Service for content generation"""
    
    def __init__(self):
        # Initialize OpenAI
        self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Initialize Gemini
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.gemini_model = genai.GenerativeModel(settings.GEMINI_MODEL)
    
    async def generate_with_openai(
        self,
        prompt: str,
        system_message: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> str:
        """Generate content using OpenAI GPT"""
        try:
            messages = []
            
            if system_message:
                messages.append({"role": "system", "content": system_message})
            
            messages.append({"role": "user", "content": prompt})
            
            response = await self.openai_client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            raise Exception(f"OpenAI generation failed: {str(e)}")
    
    async def generate_with_gemini(
        self,
        prompt: str,
        temperature: float = 0.7
    ) -> str:
        """Generate content using Google Gemini"""
        try:
            generation_config = {
                "temperature": temperature,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 2048,
            }
            
            response = await self.gemini_model.generate_content_async(
                prompt,
                generation_config=generation_config
            )
            
            return response.text
        
        except Exception as e:
            raise Exception(f"Gemini generation failed: {str(e)}")
    
    async def generate_research_introduction(
        self,
        title: str,
        field_of_study: str,
        language: str = "ar",
        provider: str = "openai"
    ) -> str:
        """Generate research introduction"""
        
        if language == "ar":
            system_message = "أنت مساعد أكاديمي متخصص في كتابة البحوث الجامعية باللغة العربية."
            prompt = f"""اكتب مقدمة أكاديمية متقنة لبحث بعنوان: "{title}"
في مجال: {field_of_study}

يجب أن تتضمن المقدمة:
1. تمهيد عام حول الموضوع
2. أهمية البحث
3. الأهداف الرئيسية
4. نطاق البحث
5. خطة البحث

اكتب بأسلوب أكاديمي رسمي ومتماسك."""
        else:
            system_message = "You are an academic assistant specialized in writing university research papers."
            prompt = f"""Write a professional academic introduction for a research paper titled: "{title}"
Field of study: {field_of_study}

The introduction should include:
1. General overview of the topic
2. Research significance
3. Main objectives
4. Research scope
5. Research outline

Write in a formal academic style."""
        
        if provider == "openai":
            return await self.generate_with_openai(prompt, system_message)
        else:
            return await self.generate_with_gemini(prompt)
    
    async def generate_research_conclusion(
        self,
        title: str,
        content_summary: str,
        language: str = "ar",
        provider: str = "openai"
    ) -> str:
        """Generate research conclusion"""
        
        if language == "ar":
            system_message = "أنت مساعد أكاديمي متخصص في كتابة البحوث الجامعية باللغة العربية."
            prompt = f"""اكتب خاتمة أكاديمية متقنة لبحث بعنوان: "{title}"

ملخص المحتوى:
{content_summary}

يجب أن تتضمن الخاتمة:
1. ملخص للنتائج الرئيسية
2. الاستنتاجات المستخلصة
3. التوصيات
4. المقترحات للبحوث المستقبلية

اكتب بأسلوب أكاديمي رسمي."""
        else:
            system_message = "You are an academic assistant specialized in writing university research papers."
            prompt = f"""Write a professional academic conclusion for a research paper titled: "{title}"

Content summary:
{content_summary}

The conclusion should include:
1. Summary of main findings
2. Key conclusions
3. Recommendations
4. Suggestions for future research

Write in a formal academic style."""
        
        if provider == "openai":
            return await self.generate_with_openai(prompt, system_message)
        else:
            return await self.generate_with_gemini(prompt)
    
    async def improve_text(
        self,
        text: str,
        language: str = "ar",
        provider: str = "openai"
    ) -> str:
        """Improve academic text"""
        
        if language == "ar":
            system_message = "أنت محرر أكاديمي متخصص في تحسين النصوص الأكاديمية."
            prompt = f"""قم بتحسين النص التالي من الناحية الأكاديمية:

{text}

احتفظ بالمعنى الأصلي وحسّن:
1. الصياغة والأسلوب
2. التماسك والترابط
3. الدقة الأكاديمية
4. وضوح التعبير"""
        else:
            system_message = "You are an academic editor specialized in improving academic texts."
            prompt = f"""Improve the following text academically:

{text}

Keep the original meaning and improve:
1. Phrasing and style
2. Coherence and flow
3. Academic precision
4. Clarity of expression"""
        
        if provider == "openai":
            return await self.generate_with_openai(prompt, system_message, temperature=0.3)
        else:
            return await self.generate_with_gemini(prompt)
    
    async def check_grammar(
        self,
        text: str,
        language: str = "ar"
    ) -> Dict[str, any]:
        """Check grammar and provide corrections"""
        
        if language == "ar":
            system_message = "أنت مدقق لغوي متخصص في اللغة العربية."
            prompt = f"""قم بمراجعة النص التالي وتصحيح الأخطاء اللغوية والنحوية:

{text}

قدم:
1. النص المصحح
2. قائمة بالأخطاء المكتشفة
3. تفسير للتصحيحات"""
        else:
            system_message = "You are a professional proofreader."
            prompt = f"""Review the following text and correct grammar mistakes:

{text}

Provide:
1. Corrected text
2. List of errors found
3. Explanation of corrections"""
        
        result = await self.generate_with_openai(prompt, system_message, temperature=0.2)
        
        return {
            "original_text": text,
            "corrected_text": result,
            "language": language
        }


# Create singleton instance
ai_service = AIService()
