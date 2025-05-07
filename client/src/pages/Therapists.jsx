// src/pages/Therapists.jsx
import React, { useEffect, useState } from 'react';
import { fetchTherapists } from '../services/api';
import '../styles/therapists.css';

export default function Therapists() {
  const [list, setList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTherapists()
      .then(r => setList(r.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Завантаження…</div>;

  return (
    <div className="therapists">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">
            therapy<br />platform
          </h1>
          <nav className="nav">
            <ul>
              <li>
                <a href="#" className="text-wrapper">
                  психологи
                </a>
              </li>
              <li>
                <a href="#" className="div">
                  чат
                </a>
              </li>
              <li>
                <a href="#" className="text-wrapper-2">
                  профіль
                </a>
              </li>
            </ul>
          </nav>
          <a
            href="tel:+380000000000"
            className="call-icon"
            aria-label="Зателефонувати"
          >
            <img
              className="phone-call-img"
              src="https://c.animaapp.com/m8of8lb90J94Ha/img/phone-call-img.png"
              alt="Іконка телефону"
            />
          </a>
        </div>
      </aside>

      {/* Main content */}
      <main>
        {list.map(t => (
          <section key={t.id} className="view overlap-2">
            {t.best && <div className="best-match">Best match</div>}

            <div className="psychol-info">
              <div className="psychol-img-container">
                <img
                  className="psychol-img"
                  src={t.photo}
                  alt={`Фото ${t.name}`}
                />
              </div>
              <div className="psychol-details">
                <h3 className="psychol-name">{t.name}</h3>
                <div className="psychol-profession">{t.profession}</div>
                <div className="psychol-text">{t.bio}</div>
              </div>
            </div>

            <div className="overlap-group-wrapper">
              <button className="write-button">
                <div className="overlap-group-2">
                  <div className="text-wrapper-4">Написати</div>
                </div>
              </button>
            </div>
          </section>
        ))}
      </main>
    </div>
  );
}
