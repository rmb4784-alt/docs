import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from 'sonner';
import { useAuthStore } from './hooks/useAuth';
import { HomePage } from './pages/Home';
import { LoginPage } from './pages/Login';
import { RegisterPage } from './pages/Register';
import './styles/index.css';

// Create a query client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
});

// Protected Route Component
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);
  
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  
  return <>{children}</>;
};

// Dashboard Placeholder
const DashboardPage: React.FC = () => {
  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);
  
  return (
    <div className="min-h-screen bg-gray-50" dir="rtl">
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold font-arabic">لوحة التحكم</h1>
          <div className="flex items-center gap-4">
            <span className="font-arabic text-gray-700">مرحباً، {user?.full_name || user?.username}</span>
            <button onClick={logout} className="btn-secondary font-arabic">
              تسجيل الخروج
            </button>
          </div>
        </div>
      </header>
      
      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="card">
            <h3 className="text-xl font-bold mb-2 font-arabic">بحث جديد</h3>
            <p className="text-gray-600 mb-4 font-arabic">ابدأ بحثك الجامعي الجديد</p>
            <button className="btn-primary w-full font-arabic">إنشاء بحث</button>
          </div>
          
          <div className="card">
            <h3 className="text-xl font-bold mb-2 font-arabic">بحوثي</h3>
            <p className="text-gray-600 mb-4 font-arabic">عرض جميع بحوثك الحالية</p>
            <button className="btn-secondary w-full font-arabic">عرض البحوث</button>
          </div>
          
          <div className="card">
            <h3 className="text-xl font-bold mb-2 font-arabic">أدوات الذكاء الاصطناعي</h3>
            <p className="text-gray-600 mb-4 font-arabic">استخدم أدوات التوليد الذكي</p>
            <button className="btn-secondary w-full font-arabic">الأدوات</button>
          </div>
        </div>
        
        <div className="mt-8 card">
          <h2 className="text-2xl font-bold mb-4 font-arabic">البحوث الأخيرة</h2>
          <p className="text-gray-600 font-arabic">لا توجد بحوث حالياً. ابدأ بإنشاء بحثك الأول!</p>
        </div>
      </main>
    </div>
  );
};

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Toaster position="top-center" richColors />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route 
            path="/dashboard" 
            element={
              <ProtectedRoute>
                <DashboardPage />
              </ProtectedRoute>
            } 
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
