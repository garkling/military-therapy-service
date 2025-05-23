import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchProfile, updateProfile } from '../services/api';
import '../styles/soldier.css';

export default function ProfilePage() {
  const [profile, setProfile] = useState({
    firstName: '', lastName: '', photo: '', nickname: '', email: '', location: '', problems: ''
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProfile()
      .then(r => setProfile(r.data))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const handleChange = e => {
    const { name, value } = e.target;
    setProfile(p => ({ ...p, [name]: value }));
  };

  const handleSubmit = e => {
    e.preventDefault();
    updateProfile(profile)
      .then(() => alert('Профіль оновлено'))
      .catch(() => alert('Помилка оновлення'));
  };

  if (loading) return <div>Завантаження…</div>;

  return (
    <div className="page-container">
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">PHOENIX</h1>
          <nav className="nav">
            <ul>
              <li>
                <Link to="/therapists" className="text-wrapper">
                  психологи
                </Link>
              </li>
              <li>
                <Link to="/profile" className="text-wrapper-2">
                  профіль
                </Link>
              </li>
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

      <main className="main-content">
        <section className="profile-section">
          <div className="profile-image-container">
            <img src={profile.photo || 'https://i.pinimg.com/…jpg'} alt="Profile" />
            <h2>{`${profile.lastName} ${profile.firstName}`}</h2>
            <p className="profile-rank">бойовий</p>
          </div>
          <div className="info-section">
            <h2>Особиста інформація</h2>
            <form onSubmit={handleSubmit} className="info-form">
              <div className="form-row">
                <input name="lastName"   value={profile.lastName}   onChange={handleChange} />
                <input name="firstName"  value={profile.firstName}  onChange={handleChange} />
              </div>
              <div className="form-row">
                <input name="nickname"   value={profile.nickname}   onChange={handleChange} />
                <input name="email"      value={profile.email}      onChange={handleChange} />
              </div>
              <input name="location"    value={profile.location}  onChange={handleChange} />
              <textarea name="problems" rows="2" value={profile.problems} onChange={handleChange} />
              <button type="submit" className="submit-btn">Змінити</button>
            </form>
          </div>
        </section>
      </main>
    </div>
  );
}
