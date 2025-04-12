// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Homepage from './pages/homepage'; // Зверни увагу, ім'я файлу (Homepage.jsx) повинно співпадати з іменем імпортованого компонента
import EmailPage from './pages/EmailPage';
import CodePage from './pages/CodePage';
import AccountPage from './pages/AccountPage';
import Test from './pages/Test';
import './App.css';
import './styles.css';

function App() {
  return (
    <Router>
      <Routes>
        {/* Головна сторінка */}
        <Route path="/" element={<Homepage />} />
        {/* Сторінка логіну */}
        <Route path="/login" element={<EmailPage />} />
        {/* Інші сторінки */}
        <Route path="/code" element={<CodePage />} />
        <Route path="/create-account" element={<AccountPage />} />
        <Route path="/test" element={<Test />} />
      </Routes>
    </Router>
  );
}

export default App;
