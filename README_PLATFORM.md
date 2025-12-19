# منصة إنجاز البحوث الجامعية - AI Research Platform 🎓🤖

<div dir="rtl">

## 📖 نظرة عامة

منصة متكاملة لإنجاز البحوث الجامعية باستخدام الذكاء الاصطناعي. توفر المنصة أدوات شاملة للطلاب والباحثين لإنشاء بحوث أكاديمية عالية الجودة بسهولة وسرعة.

## ✨ الميزات الرئيسية

### 🤖 الذكاء الاصطناعي
- **توليد المحتوى البحثي**: إنشاء مقدمات، فصول، وخاتمات باستخدام GPT-4 و Gemini
- **التدقيق اللغوي**: تصحيح لغوي ونحوي متقدم
- **إعادة الصياغة**: إعادة صياغة النصوص بأسلوب أكاديمي
- **التلخيص**: تلخيص النصوص الطويلة
- **تحسين الأسلوب**: تحسين الصياغة الأكاديمية

### 📚 إدارة المراجع
- إضافة وإدارة المراجع الأكاديمية
- دعم أنماط الاقتباس المختلفة (APA, MLA, Chicago, Harvard, IEEE)
- تنسيق المراجع تلقائياً
- استيراد المراجع من قواعد البيانات

### 📝 محرر النصوص
- محرر نصوص غني بالميزات
- دعم التنسيق الأكاديمي
- حفظ تلقائي للمسودات
- تتبع عدد الكلمات

### 📊 إدارة المشاريع
- إنشاء وإدارة مشاريع البحث
- تنظيم الأقسام والفصول
- تتبع حالة البحث
- حفظ المسودات

### 📤 التصدير
- تصدير البحوث بصيغة PDF
- تصدير بصيغة DOCX
- قوالب جاهزة للجامعات المختلفة

## 🏗️ البنية التقنية

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **AI Services**: OpenAI GPT-4, Google Gemini

### Frontend
- **Framework**: React 18 + TypeScript
- **State Management**: Zustand
- **Routing**: React Router v6
- **Data Fetching**: TanStack Query
- **Styling**: Tailwind CSS
- **Forms**: React Hook Form + Zod
- **Editor**: TipTap
- **UI Icons**: Lucide React

### DevOps
- Docker & Docker Compose
- Nginx (Reverse Proxy)
- GitHub Actions (CI/CD)

## 🚀 البدء السريع

### المتطلبات الأساسية
```bash
- Docker & Docker Compose
- Node.js 18+ (للتطوير المحلي)
- Python 3.11+ (للتطوير المحلي)
- PostgreSQL 15+ (للتطوير المحلي)
- Redis 7+ (للتطوير المحلي)
```

### التثبيت باستخدام Docker (الطريقة الموصى بها)

1. **استنساخ المشروع**
```bash
git clone <repository-url>
cd webapp
```

2. **إعداد ملف البيئة**
```bash
# نسخ ملف البيئة النموذجي
cp backend/.env.example backend/.env

# تحديث المفاتيح في backend/.env
nano backend/.env
```

3. **إضافة مفاتيح API المطلوبة في `.env`**
```env
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
SECRET_KEY=your-secret-key-here
```

4. **تشغيل المشروع**
```bash
docker-compose up -d
```

5. **الوصول للتطبيق**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### التثبيت المحلي (للتطوير)

#### Backend Setup

```bash
cd backend

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# تثبيت المكتبات
pip install -r requirements.txt

# إعداد قاعدة البيانات
# تأكد من تشغيل PostgreSQL و Redis

# تشغيل الخادم
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend

# تثبيت المكتبات
npm install

# تشغيل خادم التطوير
npm run dev
```

## 📖 البنية الكودية

```
webapp/
├── backend/                 # Backend API
│   ├── app/
│   │   ├── main.py         # نقطة الدخول الرئيسية
│   │   ├── config.py       # إعدادات التطبيق
│   │   ├── database.py     # إعدادات قاعدة البيانات
│   │   ├── models/         # نماذج البيانات
│   │   │   ├── user.py
│   │   │   ├── research.py
│   │   │   └── reference.py
│   │   ├── routers/        # API Routes
│   │   │   ├── auth.py
│   │   │   ├── research.py
│   │   │   ├── ai_generation.py
│   │   │   └── references.py
│   │   ├── services/       # خدمات الأعمال
│   │   │   └── ai_service.py
│   │   └── utils/          # أدوات مساعدة
│   │       ├── security.py
│   │       └── helpers.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/               # Frontend App
│   ├── src/
│   │   ├── components/    # مكونات React
│   │   ├── pages/         # صفحات التطبيق
│   │   │   ├── Home.tsx
│   │   │   ├── Login.tsx
│   │   │   └── Register.tsx
│   │   ├── services/      # خدمات API
│   │   │   └── api.ts
│   │   ├── hooks/         # React Hooks
│   │   │   └── useAuth.ts
│   │   ├── utils/         # أدوات مساعدة
│   │   ├── styles/        # ملفات CSS
│   │   ├── App.tsx        # المكون الرئيسي
│   │   └── main.tsx       # نقطة الدخول
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── docker-compose.yml     # إعدادات Docker
├── PROJECT_PLAN.md        # خطة المشروع
└── README.md              # هذا الملف
```

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - تسجيل مستخدم جديد
- `POST /api/auth/login` - تسجيل الدخول
- `GET /api/auth/me` - الحصول على معلومات المستخدم
- `PUT /api/auth/me` - تحديث معلومات المستخدم

### Research
- `POST /api/research/` - إنشاء بحث جديد
- `GET /api/research/` - قائمة البحوث
- `GET /api/research/{id}` - الحصول على بحث محدد
- `PUT /api/research/{id}` - تحديث بحث
- `DELETE /api/research/{id}` - حذف بحث

### AI Generation
- `POST /api/ai/generate/introduction` - توليد مقدمة
- `POST /api/ai/generate/conclusion` - توليد خاتمة
- `POST /api/ai/improve` - تحسين النص
- `POST /api/ai/check-grammar` - التدقيق اللغوي
- `POST /api/ai/paraphrase` - إعادة الصياغة
- `POST /api/ai/summarize` - التلخيص

### References
- `POST /api/references/` - إضافة مرجع
- `GET /api/references/research/{research_id}` - قائمة مراجع البحث
- `PUT /api/references/{id}` - تحديث مرجع
- `DELETE /api/references/{id}` - حذف مرجع
- `POST /api/references/format-citation` - تنسيق اقتباس

## 🔐 الأمان

- JWT Authentication لتأمين API
- تشفير كلمات المرور باستخدام bcrypt
- CORS middleware للتحكم في الوصول
- Rate limiting لمنع إساءة الاستخدام
- Validation شاملة للمدخلات

## 🧪 الاختبار

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 📈 خارطة الطريق

- [x] البنية الأساسية للمشروع
- [x] نظام المصادقة والمستخدمين
- [x] إدارة البحوث والأقسام
- [x] تكامل الذكاء الاصطناعي (OpenAI & Gemini)
- [x] نظام المراجع والاقتباسات
- [ ] محرر نصوص متقدم
- [ ] فحص السرقة الأدبية
- [ ] تصدير PDF و DOCX
- [ ] القوالب الأكاديمية
- [ ] البحث في قواعد البيانات الأكاديمية
- [ ] التعاون بين الباحثين
- [ ] التطبيق المحمول

## 🤝 المساهمة

نرحب بجميع المساهمات! يرجى:

1. Fork المشروع
2. إنشاء فرع للميزة الجديدة (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. Push إلى الفرع (`git push origin feature/AmazingFeature`)
5. فتح Pull Request

## 📄 الترخيص

هذا المشروع مرخص تحت MIT License - انظر ملف [LICENSE](LICENSE) للتفاصيل.

## 👥 الفريق

منصة مفتوحة المصدر للمجتمع الأكاديمي العربي

## 📞 الدعم

إذا واجهت أي مشاكل أو لديك اقتراحات:
- افتح Issue في GitHub
- راسلنا على البريد الإلكتروني
- انضم إلى مجموعة Discord

## 🙏 شكر خاص

- OpenAI لتوفير GPT-4 API
- Google لتوفير Gemini API
- المجتمع المفتوح المصدر

---

صُنع بـ ❤️ للمجتمع الأكاديمي العربي

</div>
