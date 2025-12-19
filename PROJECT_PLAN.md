# منصة إنجاز البحوث الجامعية - AI Research Platform

## 📋 نظرة عامة
منصة متكاملة لإنجاز البحوث الجامعية باستخدام الذكاء الاصطناعي، توفر أدوات شاملة للطلاب والباحثين لإنشاء بحوث أكاديمية عالية الجودة.

## 🎯 الميزات الرئيسية

### 1. توليد المحتوى البحثي
- إنشاء مقدمات بحثية متقنة
- توليد الفصول والأقسام
- صياغة الخاتمة والتوصيات
- دعم اللغتين العربية والإنجليزية

### 2. البحث والمراجع الأكاديمية
- البحث في قواعد البيانات الأكاديمية
- توليد قائمة المراجع تلقائياً
- دعم أنماط الاقتباس المختلفة (APA, MLA, Chicago, Harvard)
- التحقق من صحة المراجع

### 3. التدقيق اللغوي والجودة
- التدقيق اللغوي والنحوي
- فحص السرقة الأدبية
- تحسين الأسلوب الأكاديمي
- اقتراحات لتحسين الصياغة

### 4. التنسيق والتصدير
- تنسيق البحث حسب المعايير الأكاديمية
- تصدير بصيغ متعددة (PDF, DOCX, LaTeX)
- قوالب جاهزة للجامعات المختلفة

### 5. إدارة المشاريع
- حفظ المسودات
- تتبع التقدم
- التعاون بين الباحثين
- نظام المراجعة والتعليقات

## 🏗️ البنية التقنية

### Backend (Python FastAPI)
```
backend/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── research.py
│   │   └── reference.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── research.py
│   │   ├── ai_generation.py
│   │   ├── references.py
│   │   └── export.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── research_generator.py
│   │   ├── reference_manager.py
│   │   ├── plagiarism_checker.py
│   │   └── export_service.py
│   └── utils/
│       ├── security.py
│       └── helpers.py
├── requirements.txt
└── .env.example
```

### Frontend (React + TypeScript)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Editor/
│   │   ├── ResearchWizard/
│   │   ├── ReferenceManager/
│   │   └── Dashboard/
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── NewResearch.tsx
│   │   ├── MyResearches.tsx
│   │   └── Settings.tsx
│   ├── services/
│   │   └── api.ts
│   ├── hooks/
│   ├── utils/
│   └── App.tsx
├── package.json
└── tsconfig.json
```

## 🤖 خدمات الذكاء الاصطناعي

### 1. OpenAI GPT-4
- توليد المحتوى البحثي
- التدقيق اللغوي
- إعادة الصياغة

### 2. Google Gemini
- تحليل المحتوى
- البحث والاستخلاص
- التلخيص

### 3. خدمات إضافية
- فحص السرقة الأدبية
- توليد المراجع
- البحث الأكاديمي

## 🗄️ قاعدة البيانات (PostgreSQL)

### الجداول الرئيسية:
- **users**: المستخدمون
- **researches**: البحوث
- **sections**: أقسام البحث
- **references**: المراجع
- **templates**: القوالب
- **drafts**: المسودات

## 🔐 الأمان والمصادقة
- JWT Authentication
- تشفير كلمات المرور
- حماية API
- Rate limiting

## 📦 التقنيات المستخدمة

### Backend
- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Redis (للذاكرة المؤقتة)
- OpenAI API
- Google Gemini API

### Frontend
- React 18+
- TypeScript
- Tailwind CSS
- React Query
- Zustand (إدارة الحالة)
- React Router
- Axios
- Rich Text Editor (TipTap أو Quill)

### DevOps
- Docker
- Docker Compose
- Nginx
- GitHub Actions (CI/CD)

## 🚀 خطة التطوير

### المرحلة 1: الإعداد الأساسي
- [x] تصميم البنية التقنية
- [ ] إعداد Backend API
- [ ] إعداد Frontend
- [ ] إعداد قاعدة البيانات

### المرحلة 2: الميزات الأساسية
- [ ] نظام المصادقة
- [ ] إنشاء البحث الأساسي
- [ ] محرر النصوص
- [ ] حفظ المسودات

### المرحلة 3: الذكاء الاصطناعي
- [ ] دمج OpenAI
- [ ] دمج Gemini
- [ ] توليد المحتوى
- [ ] التدقيق اللغوي

### المرحلة 4: المراجع والاقتباسات
- [ ] نظام المراجع
- [ ] أنماط الاقتباس
- [ ] البحث الأكاديمي

### المرحلة 5: التصدير والتنسيق
- [ ] تصدير PDF
- [ ] تصدير DOCX
- [ ] القوالب الأكاديمية

### المرحلة 6: الميزات المتقدمة
- [ ] فحص السرقة الأدبية
- [ ] التعاون بين الباحثين
- [ ] الإحصائيات والتحليلات

## 📝 متطلبات التشغيل

### Backend
```bash
Python 3.11+
PostgreSQL 14+
Redis 7+
```

### Frontend
```bash
Node.js 18+
npm أو yarn
```

## 🔧 التثبيت والتشغيل

### 1. Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Docker (الطريقة الموصى بها)
```bash
docker-compose up -d
```

## 🌐 الروابط

- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432

## 📄 الترخيص
MIT License

## 👥 الفريق
منصة مفتوحة المصدر للمجتمع الأكاديمي العربي
