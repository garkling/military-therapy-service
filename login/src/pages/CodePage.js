// src/pages/CodePage.js
import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const CodePage = () => {
  const [code, setCode] = useState('');
  const navigate = useNavigate();
  const location = useLocation();
  const email = location.state?.email || '';

  const handleCodeSubmit = () => {
    if (!code.trim()) {
      alert('Будь ласка, введіть код');
      return;
    }

    navigate('/create-account', { state: { email, code } });
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
        <button onClick={handleCodeSubmit}>Далі</button>
      </div>
    </div>
  );
};

export default CodePage;
