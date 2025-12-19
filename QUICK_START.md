# دليل البدء السريع - منصة إنجاز البحوث الجامعية 🚀

## المتطلبات الأساسية
- Docker & Docker Compose مثبت على جهازك
- مفاتيح API من OpenAI و Google (Gemini)

## خطوات التشغيل السريعة

### 1️⃣ إعداد مفاتيح API

قم بإنشاء ملف `.env` في مجلد `backend`:

```bash
cp backend/.env.example backend/.env
```

ثم قم بتعديل الملف وإضافة مفاتيحك:

```env
# أضف مفاتيح API الخاصة بك
OPENAI_API_KEY=sk-your-openai-api-key-here
GOOGLE_API_KEY=your-google-gemini-api-key-here

# يمكنك تغيير هذا المفتاح السري
SECRET_KEY=your-very-secret-key-change-this-in-production
```

### 2️⃣ تشغيل المنصة

```bash
# تشغيل جميع الخدمات
docker-compose up -d

# عرض السجلات (logs)
docker-compose logs -f
```

### 3️⃣ الوصول للمنصة

بعد دقيقة أو دقيقتين، ستكون المنصة جاهزة:

- **الواجهة الأمامية (Frontend)**: http://localhost:3000
- **API الخلفية (Backend)**: http://localhost:8000
- **توثيق API**: http://localhost:8000/docs

### 4️⃣ إنشاء حساب جديد

1. افتح http://localhost:3000
2. اضغط على "إنشاء حساب"
3. املأ البيانات المطلوبة
4. ابدأ باستخدام المنصة!

## أوامر مفيدة

```bash
# إيقاف المنصة
docker-compose down

# إيقاف وحذف البيانات
docker-compose down -v

# إعادة بناء الصور
docker-compose up -d --build

# عرض حالة الخدمات
docker-compose ps

# عرض سجلات خدمة معينة
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f postgres
```

## استكشاف الأخطاء

### مشكلة: Backend لا يعمل
```bash
# تحقق من السجلات
docker-compose logs backend

# تأكد من إعداد مفاتيح API في .env
cat backend/.env
```

### مشكلة: قاعدة البيانات لا تتصل
```bash
# أعد تشغيل قاعدة البيانات
docker-compose restart postgres

# تحقق من حالة PostgreSQL
docker-compose exec postgres pg_isready -U research_user
```

### مشكلة: Frontend لا يظهر
```bash
# أعد بناء Frontend
docker-compose up -d --build frontend

# تحقق من السجلات
docker-compose logs -f frontend
```

## استخدام API مباشرة

### تسجيل مستخدم جديد
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "securepassword123",
    "full_name": "اسم المستخدم"
  }'
```

### تسجيل الدخول
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "securepassword123"
  }'
```

### توليد مقدمة بحثية
```bash
# احصل أولاً على token من تسجيل الدخول
TOKEN="your-access-token-here"

curl -X POST http://localhost:8000/api/ai/generate/introduction \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "الذكاء الاصطناعي في التعليم",
    "field_of_study": "تكنولوجيا التعليم",
    "language": "ar",
    "provider": "openai"
  }'
```

## الميزات المتاحة

✅ **جاهزة للاستخدام:**
- تسجيل المستخدمين والدخول
- إنشاء وإدارة البحوث
- توليد المحتوى البحثي بالذكاء الاصطناعي
- إدارة المراجع والاقتباسات
- التدقيق اللغوي
- إعادة الصياغة والتلخيص

🚧 **قيد التطوير:**
- محرر نصوص متقدم
- تصدير PDF/DOCX
- فحص السرقة الأدبية
- القوالب الأكاديمية

## الحصول على مفاتيح API

### OpenAI API Key
1. انتقل إلى https://platform.openai.com
2. سجل حساب أو سجل دخولك
3. انتقل إلى API Keys
4. أنشئ مفتاح جديد

### Google Gemini API Key
1. انتقل إلى https://makersuite.google.com/app/apikey
2. سجل حساب أو سجل دخولك
3. أنشئ مفتاح API جديد

## دعم فني

إذا واجهت أي مشاكل:
1. تحقق من السجلات: `docker-compose logs`
2. تأكد من إعداد مفاتيح API بشكل صحيح
3. أعد تشغيل الخدمات: `docker-compose restart`
4. افتح issue في GitHub

---

🎓 **منصة مفتوحة المصدر للمجتمع الأكاديمي العربي**

للمزيد من التفاصيل، راجع [README_PLATFORM.md](README_PLATFORM.md)
