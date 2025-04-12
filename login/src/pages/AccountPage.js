// src/pages/AccountPage.js
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

const AccountPage = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const location = useLocation();
  const email = location.state?.email || '';
  const code = location.state?.code || '';

  const handleCreateAccount = () => {
    if (!firstName.trim() || !lastName.trim()) {
      alert("Будь ласка, заповніть і ім'я, і прізвище");
      return;
    }
    alert('Аккаунт успішно створено!');
    // Тут інша логіка (API виклик і т.д.)
  };

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Створи аккаунт</h2>
        <input
          type="text"
          placeholder="Прізвище"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Імʼя"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <button onClick={handleCreateAccount}>Створити аккаунт</button>
      </div>
    </div>
  );
};

export default AccountPage;
