import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuthStore } from '@/hooks/useAuth';
import { authAPI } from '@/services/api';
import { toast } from 'sonner';

export const RegisterPage: React.FC = () => {
  const navigate = useNavigate();
  const setAuth = useAuthStore((state) => state.setAuth);
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    full_name: '',
    university: '',
    major: '',
    academic_level: 'bachelor',
  });
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await authAPI.register(formData);
      const { access_token, user } = response.data;
      
      setAuth(user, access_token);
      toast.success('تم إنشاء الحساب بنجاح');
      navigate('/dashboard');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'فشل إنشاء الحساب');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 to-primary-100 px-4 py-8" dir="rtl">
      <div className="max-w-2xl w-full bg-white rounded-2xl shadow-xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 font-arabic mb-2">
            إنشاء حساب جديد
          </h1>
          <p className="text-gray-600 font-arabic">
            انضم إلى منصة البحوث الجامعية الذكية
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label htmlFor="full_name" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
                الاسم الكامل
              </label>
              <input
                id="full_name"
                type="text"
                required
                className="input font-arabic"
                value={formData.full_name}
                onChange={(e) => setFormData({ ...formData, full_name: e.target.value })}
                placeholder="أدخل اسمك الكامل"
              />
            </div>

            <div>
              <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
                اسم المستخدم
              </label>
              <input
                id="username"
                type="text"
                required
                className="input font-arabic"
                value={formData.username}
                onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                placeholder="اختر اسم مستخدم"
              />
            </div>
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
              البريد الإلكتروني
            </label>
            <input
              id="email"
              type="email"
              required
              className="input font-arabic"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              placeholder="example@university.edu"
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
              كلمة المرور
            </label>
            <input
              id="password"
              type="password"
              required
              className="input font-arabic"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              placeholder="اختر كلمة مرور قوية"
            />
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label htmlFor="university" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
                الجامعة
              </label>
              <input
                id="university"
                type="text"
                className="input font-arabic"
                value={formData.university}
                onChange={(e) => setFormData({ ...formData, university: e.target.value })}
                placeholder="اسم الجامعة"
              />
            </div>

            <div>
              <label htmlFor="major" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
                التخصص
              </label>
              <input
                id="major"
                type="text"
                className="input font-arabic"
                value={formData.major}
                onChange={(e) => setFormData({ ...formData, major: e.target.value })}
                placeholder="التخصص الدراسي"
              />
            </div>
          </div>

          <div>
            <label htmlFor="academic_level" className="block text-sm font-medium text-gray-700 mb-2 font-arabic">
              المستوى الأكاديمي
            </label>
            <select
              id="academic_level"
              className="input font-arabic"
              value={formData.academic_level}
              onChange={(e) => setFormData({ ...formData, academic_level: e.target.value })}
            >
              <option value="bachelor">بكالوريوس</option>
              <option value="master">ماجستير</option>
              <option value="phd">دكتوراه</option>
            </select>
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full btn-primary font-arabic text-lg py-3 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? 'جاري إنشاء الحساب...' : 'إنشاء حساب'}
          </button>

          <div className="text-center text-sm text-gray-600 font-arabic">
            لديك حساب بالفعل؟{' '}
            <Link to="/login" className="text-primary-600 hover:text-primary-700 font-medium">
              سجل دخولك
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
};
