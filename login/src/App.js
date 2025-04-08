// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import EmailPage from './pages/EmailPage';
import CodePage from './pages/CodePage';
import AccountPage from './pages/AccountPage';
import './App.css';
import './styles.css';

function App() {
  return (
    <Router>
      <div className="center-container">
        <Routes>
          <Route path="/" element={<EmailPage />} />
          <Route path="/code" element={<CodePage />} />
          <Route path="/create-account" element={<AccountPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
