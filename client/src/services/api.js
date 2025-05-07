/*
src/services/api.js
*/
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  headers: { 'Content-Type': 'application/json' },
  timeout: 10000,
});

api.interceptors.request.use(cfg => {
  const token = localStorage.getItem('access_token');
  if (token) cfg.headers.Authorization = `Bearer ${token}`;
  return cfg;
});

export const createAccount   = data => api.post('/users', data);
export const submitTest      = answers => api.post('/assessment', { answers });
export const fetchTherapists = () => api.get('/users/therapists');
export const fetchProfile    = () => api.get('/users/me');
export const updateProfile   = data => api.put('/users', data);

export default api;


