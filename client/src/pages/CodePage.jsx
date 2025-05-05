// src/pages/CodePage.jsx
import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { verifyAuthCode } from '../services/auth';
import '../styles/code.css';

export default function CodePage() {
  const [code, setCode] = useState('');
  const [loading, setLoading] = useState(false);
  const { state } = useLocation();
  const navigate = useNavigate();

  const email = state?.email;

  const handleVerify = async () => {
    if (!code) {
      alert('Введіть код з листа');
      return;
    }

    setLoading(true);

    try {
      const response = await verifyAuthCode(email, code);
      const { access_token, id_token } = response.data;

      // Зберігаємо токени
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('id_token', id_token);

      // Переходимо до сторінки створення акаунта
      navigate('/create-account', { state: { email, code } });
    } catch (error) {
      console.error('[verifyAuthCode error]', error);
      const msg = error.response?.data?.error_description || 'Невірний код';
      alert(`Помилка: ${msg}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Введіть код</h2>
        <input
          type="text"
          placeholder="Ваш код"
          value={code}
          onChange={(e) => setCode(e.target.value)}
        />
        <button onClick={handleVerify} disabled={loading}>
          {loading ? 'Перевірка…' : 'Перевірити'}
        </button>
      </div>
    </div>
  );
}
