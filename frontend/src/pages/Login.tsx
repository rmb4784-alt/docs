import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuthStore } from '@/hooks/useAuth';
import { authAPI } from '@/services/api';
import { toast } from 'sonner';

export const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const setAuth = useAuthStore((state) => state.setAuth);
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await authAPI.login(formData);
      const { access_token, user } = response.data;
      
      setAuth(user, access_token);
      toast.success('تم تسجيل الدخول بنجاح');
      navigate('/dashboard');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'فشل تسجيل الدخول');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 to-primary-100 px-4" dir="rtl">
      <div className="max-w-md w-full bg-white rounded-2xl shadow-xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 font-arabic mb-2">
            منصة البحوث الجامعية
          </h1>
          <p className="text-gray-600 font-arabic">
            سجل دخولك للوصول إلى أدوات البحث الذكية
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
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
              placeholder="أدخل اسم المستخدم"
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
              placeholder="أدخل كلمة المرور"
            />
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full btn-primary font-arabic text-lg py-3 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? 'جاري تسجيل الدخول...' : 'تسجيل الدخول'}
          </button>

          <div className="text-center text-sm text-gray-600 font-arabic">
            ليس لديك حساب؟{' '}
            <Link to="/register" className="text-primary-600 hover:text-primary-700 font-medium">
              سجل الآن
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
};
