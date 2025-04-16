// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Homepage from './pages/homepage';
import EmailPage from './pages/EmailPage';
import CodePage from './pages/CodePage';
import AccountPage from './pages/AccountPage';
import Test from './pages/Test';
import Therapists from './pages/Therapists';
import ProfilePage from './pages/ProfilePage';
import ChatPage from './pages/ChatPage';


import './App.css';
import './styles.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<EmailPage />} />
        <Route path="/code" element={<CodePage />} />
        <Route path="/create-account" element={<AccountPage />} />
        <Route path="/test" element={<Test />} />
        <Route path="/therapists" element={<Therapists />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/chat" element={<ChatPage />} />
      </Routes>
    </Router>
  );
}

export default App;