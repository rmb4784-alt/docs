import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('auth_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('auth_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth API
export const authAPI = {
  register: (data: any) => api.post('/api/auth/register', data),
  login: (data: any) => api.post('/api/auth/login', data),
  getMe: () => api.get('/api/auth/me'),
  updateMe: (data: any) => api.put('/api/auth/me', data),
};

// Research API
export const researchAPI = {
  create: (data: any) => api.post('/api/research/', data),
  list: (params?: any) => api.get('/api/research/', { params }),
  get: (id: number) => api.get(`/api/research/${id}`),
  update: (id: number, data: any) => api.put(`/api/research/${id}`, data),
  delete: (id: number) => api.delete(`/api/research/${id}`),
  
  // Sections
  createSection: (researchId: number, data: any) => 
    api.post(`/api/research/${researchId}/sections`, data),
  listSections: (researchId: number) => 
    api.get(`/api/research/${researchId}/sections`),
  updateSection: (researchId: number, sectionId: number, data: any) => 
    api.put(`/api/research/${researchId}/sections/${sectionId}`, data),
  deleteSection: (researchId: number, sectionId: number) => 
    api.delete(`/api/research/${researchId}/sections/${sectionId}`),
};

// AI Generation API
export const aiAPI = {
  generateIntroduction: (data: any) => 
    api.post('/api/ai/generate/introduction', data),
  generateConclusion: (data: any) => 
    api.post('/api/ai/generate/conclusion', data),
  improveText: (data: any) => 
    api.post('/api/ai/improve', data),
  checkGrammar: (data: any) => 
    api.post('/api/ai/check-grammar', data),
  generateCustom: (data: any) => 
    api.post('/api/ai/generate/custom', data),
  paraphrase: (data: any) => 
    api.post('/api/ai/paraphrase', data),
  summarize: (data: any) => 
    api.post('/api/ai/summarize', data),
};

// References API
export const referencesAPI = {
  create: (data: any) => api.post('/api/references/', data),
  list: (researchId: number) => 
    api.get(`/api/references/research/${researchId}`),
  get: (id: number) => api.get(`/api/references/${id}`),
  update: (id: number, data: any) => 
    api.put(`/api/references/${id}`, data),
  delete: (id: number) => api.delete(`/api/references/${id}`),
  formatCitation: (data: any) => 
    api.post('/api/references/format-citation', data),
};

export default api;
