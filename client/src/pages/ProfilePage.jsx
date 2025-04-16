// src/pages/ProfilePage.jsx
import React, { useState, useEffect } from 'react';
import "../styles/soldier.css";
import { Link } from "react-router-dom";


const ProfilePage = () => {
  // Початковий стан для профілю з порожніми значеннями
  const [profile, setProfile] = useState({
    firstName: '',
    lastName: '',
    photo: '',
    nickname: '',
    email: '',
    location: '',
    problems: ''
  });

  // Отримання даних з бекенду (наприклад, із URL http://localhost:3000/api/profile)
  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await fetch('http://localhost:3000/api/profile');
        if (response.ok) {
          const data = await response.json();
          // Очікується, що отримані дані містять: firstName, lastName, photo, nickname, email, location, problems
          setProfile(data);
        } else {
          console.error('Помилка отримання даних з бекенду');
        }
      } catch (error) {
        console.error('Помилка запиту:', error);
      }
    };

    fetchProfile();
    // Якщо потрібно, можна періодично оновлювати дані через setInterval
    // const interval = setInterval(fetchProfile, 10000);
    // return () => clearInterval(interval);
  }, []);

  return (
    <div className="page-container">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">PHOENIX</h1>
          <nav className="nav">
            <ul>
              <li><Link to="/therapists" className="text-wrapper">психологи</Link></li>
              <li><Link to="/chat" className="div">чат</Link></li>
              <li><Link to="/profile" className="text-wrapper-2">профіль</Link></li>
            </ul>
          </nav>
          <a href="tel:+380000000000" className="call-icon" aria-label="Зателефонувати">
            <img
              className="phone-call-img"
              src="https://c.animaapp.com/m8of8lb90J94Ha/img/phone-call-img.png"
              alt="Іконка телефону"
            />
          </a>
        </div>
      </aside>
      
      {/* Main Content */}
      <main className="main-content">
        {/* Profile Section: Фото профілю та інформація */}
        <section className="profile-section">
          <div className="profile-image-container">
            {/* Відображення фото (або фото за замовчуванням) */}
            <img 
              src={profile.photo || "https://i.pinimg.com/736x/2c/47/d5/2c47d5dd5b532f83bb55c4cd6f5bd1ef.jpg"} 
              alt="Profile Photo" 
              className="profile-image"
            />
            {/* Відображення прізвища та імені */}
            <h2 className="profile-name">
              {(profile.lastName || 'Депутат') + " " + (profile.firstName || 'Іван')}
            </h2>
            <p className="profile-rank">бойовий</p>
          </div>
          
          <div className="info-section">
            <h2 className="info-title">Особиста інформація</h2>
            <form className="info-form">
              <div className="form-row">
                <input 
                  type="text" 
                  name="lastName" 
                  placeholder="Прізвище" 
                  className="input-field"
                  defaultValue={profile.lastName}
                />
                <input 
                  type="text" 
                  name="firstName" 
                  placeholder="Ім'я" 
                  className="input-field"
                  defaultValue={profile.firstName}
                />
              </div>
              <div className="form-row">
                <input 
                  type="text" 
                  name="nickname" 
                  placeholder="Позивний" 
                  className="input-field"
                  defaultValue={profile.nickname}
                />
                <input 
                  type="email" 
                  name="email" 
                  placeholder="E-mail" 
                  className="input-field"
                  defaultValue={profile.email}
                />
              </div>
              <input 
                type="text" 
                name="location" 
                placeholder="Місто, країна" 
                className="input-field full-width"
                defaultValue={profile.location}
              />
              <textarea 
                name="problems" 
                rows="2" 
                placeholder="Проблеми"
                className="input-field"
                defaultValue={profile.problems}
              ></textarea>
              <button type="submit" className="submit-btn">Змінити</button>
            </form>
          </div>
        </section>
      </main>
    </div>
  );
};

export default ProfilePage;
