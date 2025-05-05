
// src/pages/EmailPage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { sendAuthCode } from '../services/auth';
import '../styles/email.css';

export default function EmailPage() {
  const [email, setEmail]     = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleNext = async () => {
    if (!email.includes('@')) {
      return alert('Введіть валідний email');
    }
    setLoading(true);
    try {
      await sendAuthCode(email);
      navigate('/code', { state: { email } });
    } catch (err) {
      console.error('[sendAuthCode error]', err.message, err.response);
      alert(err.response?.data?.error_description || err.message || 'Помилка мережі');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Введіть вашу пошту</h2>
        <input
          type="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="example@gmail.com"
        />
        <button onClick={handleNext} disabled={loading}>
          {loading ? 'Надсилання…' : 'Далі'}
        </button>
      </div>
    </div>
  );
}

