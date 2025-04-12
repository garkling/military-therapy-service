// src/pages/AccountPage.js
import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const AccountPage = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const location = useLocation();
  const navigate = useNavigate();

  // Отримуємо пошту і код зі state (передані зі сторінки з кодом)
  const email = location.state?.email || '';
  const code = location.state?.code || '';

  const handleCreateAccount = () => {
    if (!firstName.trim() || !lastName.trim()) {
      alert("Будь ласка, заповніть і ім'я, і прізвище");
      return;
    }

    // Тут можна викликати API для створення акаунту — наприклад:
    // createAccount({ firstName, lastName, email, code })

    // Після успіху переходимо до тесту
    navigate('/test', {
      state: {
        firstName,
        lastName,
        email,
      },
    });
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
