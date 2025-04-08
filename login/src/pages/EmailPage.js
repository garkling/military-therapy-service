// src/pages/EmailPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const EmailPage = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleNext = async () => {
    if (!email.includes('@')) {
      alert('Будь ласка, введіть коректну пошту');
      return;
    }
    setLoading(true);

    try {
      const response = await fetch('https://dev-nzeet1cd8b6nxgvb.us.auth0.com/passwordless/start', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        body: JSON.stringify({
          client_id: 'XbLqULjdINkfSp6Wxj4a7K0RiZJxqTrC',
          connection: 'email',
          send: 'code',
          email: email,
        }),
      });

      if (!response.ok) {
        throw new Error('Не вдалося надіслати код');
      }

      // Якщо запит успішний — переходимо на сторінку введення коду
      navigate('/code', { state: { email } });
    } catch (error) {
      alert('Помилка: не вдалося надіслати код. Спробуйте пізніше.');
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
          placeholder="example@gmail.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button onClick={handleNext} disabled={loading}>
          {loading ? 'Надсилання...' : 'Далі'}
        </button>
      </div>
    </div>
  );
};

export default EmailPage;
