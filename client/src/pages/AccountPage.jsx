// src/pages/AccountPage.jsx
import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { createAccount } from '../services/api';
import '../styles/account.css';

const AccountPage = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName,  setLastName]  = useState('');
  const { email, code } = useLocation().state || {};
  const navigate = useNavigate();

  const handleCreateAccount = async () => {
    if (!firstName.trim() || !lastName.trim()) {
      return alert("Будь ласка, заповніть і ім'я, і прізвище");
    }
    try {
      await createAccount({
        first_name: firstName,
        last_name: lastName,
        email,
        code
      });
      navigate('/test', { state: { firstName, lastName, email } });
    } catch {
      alert('Не вдалося створити акаунт');
    }
  };

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Створи аккаунт</h2>
        <input
          type="text"
          placeholder="Прізвище"
          value={lastName}
          onChange={e => setLastName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Імʼя"
          value={firstName}
          onChange={e => setFirstName(e.target.value)}
        />
        <button onClick={handleCreateAccount}>Створити аккаунт</button>
      </div>
    </div>
  );
};

export default AccountPage;
