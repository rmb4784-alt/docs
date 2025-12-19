import React from 'react';
import { Link } from 'react-router-dom';
import { useAuthStore } from '@/hooks/useAuth';
import { BookOpen, Brain, FileCheck, Download, Users, Sparkles } from 'lucide-react';

export const HomePage: React.FC = () => {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-primary-50" dir="rtl">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <nav className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Brain className="w-8 h-8 text-primary-600" />
            <span className="text-2xl font-bold text-gray-900 font-arabic">منصة البحوث الجامعية</span>
          </div>
          
          <div className="flex gap-4">
            {isAuthenticated ? (
              <Link to="/dashboard" className="btn-primary font-arabic">
                لوحة التحكم
              </Link>
            ) : (
              <>
                <Link to="/login" className="btn-secondary font-arabic">
                  تسجيل الدخول
                </Link>
                <Link to="/register" className="btn-primary font-arabic">
                  إنشاء حساب
                </Link>
              </>
            )}
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20 text-center">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6 font-arabic">
            منصة متكاملة لإنجاز البحوث الجامعية
          </h1>
          <p className="text-xl text-gray-600 mb-8 font-arabic leading-relaxed">
            استخدم قوة الذكاء الاصطناعي لإنشاء بحوث أكاديمية عالية الجودة بسهولة وسرعة
          </p>
          <div className="flex gap-4 justify-center">
            <Link to="/register" className="btn-primary text-lg px-8 py-3 font-arabic">
              ابدأ الآن مجاناً
            </Link>
            <Link to="/demo" className="btn-secondary text-lg px-8 py-3 font-arabic">
              شاهد العرض التوضيحي
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="container mx-auto px-4 py-16">
        <h2 className="text-4xl font-bold text-center text-gray-900 mb-12 font-arabic">
          الميزات الرئيسية
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {/* Feature 1 */}
          <div className="card hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-primary-100 rounded-lg">
                <Sparkles className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 font-arabic">توليد المحتوى الذكي</h3>
            </div>
            <p className="text-gray-600 font-arabic leading-relaxed">
              استخدم الذكاء الاصطناعي لإنشاء مقدمات، فصول، وخاتمات بحثية متقنة بأسلوب أكاديمي احترافي
            </p>
          </div>

          {/* Feature 2 */}
          <div className="card hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-primary-100 rounded-lg">
                <BookOpen className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 font-arabic">إدارة المراجع</h3>
            </div>
            <p className="text-gray-600 font-arabic leading-relaxed">
              نظام متكامل لإدارة المراجع والاقتباسات بأنماط مختلفة (APA, MLA, Chicago, Harvard)
            </p>
          </div>

          {/* Feature 3 */}
          <div className="card hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-primary-100 rounded-lg">
                <FileCheck className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 font-arabic">التدقيق اللغوي</h3>
            </div>
            <p className="text-gray-600 font-arabic leading-relaxed">
              تدقيق لغوي ونحوي متقدم مع فحص السرقة الأدبية وتحسين الأسلوب الأكاديمي
            </p>
          </div>

          {/* Feature 4 */}
          <div className="card hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-primary-100 rounded-lg">
                <Download className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 font-arabic">تصدير احترافي</h3>
            </div>
            <p className="text-gray-600 font-arabic leading-relaxed">
              تصدير البحوث بصيغ متعددة (PDF, DOCX) مع قوالب جاهزة للجامعات المختلفة
            </p>
          </div>

          {/* Feature 5 */}
          <div className="card hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-primary-100 rounded-lg">
                <Brain className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 font-arabic">ذكاء اصطناعي متقدم</h3>
            </div>
            <p className="text-gray-600 font-arabic leading-relaxed">
              تكامل مع أقوى نماذج الذكاء الاصطناعي (GPT-4, Gemini) لضمان أعلى جودة
            </p>
          </div>

          {/* Feature 6 */}
          <div className="card hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-primary-100 rounded-lg">
                <Users className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 font-arabic">التعاون الجماعي</h3>
            </div>
            <p className="text-gray-600 font-arabic leading-relaxed">
              إمكانية التعاون بين الباحثين مع نظام المراجعة والتعليقات المتقدم
            </p>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-primary-600 text-white py-16">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-4xl font-bold mb-6 font-arabic">
            ابدأ رحلتك البحثية الآن
          </h2>
          <p className="text-xl mb-8 font-arabic">
            انضم إلى آلاف الباحثين الذين يستخدمون منصتنا لإنجاز بحوثهم الجامعية
          </p>
          <Link to="/register" className="bg-white text-primary-600 px-8 py-3 rounded-lg text-lg font-medium hover:bg-gray-100 transition-colors font-arabic inline-block">
            سجل مجاناً الآن
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="container mx-auto px-4 text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Brain className="w-6 h-6" />
            <span className="text-xl font-bold font-arabic">منصة البحوث الجامعية</span>
          </div>
          <p className="text-gray-400 font-arabic">
            منصة مفتوحة المصدر للمجتمع الأكاديمي العربي
          </p>
          <p className="text-gray-500 mt-2 font-arabic">
            © 2024 جميع الحقوق محفوظة
          </p>
        </div>
      </footer>
    </div>
  );
};
