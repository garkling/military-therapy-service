import React, { useEffect, useState } from 'react';
import { fetchTherapists } from '../services/api';
import '../styles/therapists.css';

export default function Therapists() {
  const [list, setList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTherapists()
      .then((r) => setList(r.data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Завантаження…</div>;

  // Перша психологиня як найкращий збіг
  const bestMatch = list[0];
  const others = list.slice(1);

  return (
    <div className="therapists">
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">therapy<br/>platform</h1>
          <nav className="nav">
            <ul>
              <li><a href="#" className="text-wrapper">психологи</a></li>
              <li><a href="#" className="div">чат</a></li>
              <li><a href="#" className="text-wrapper-2">профіль</a></li>
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

      <main>
        {bestMatch && (
          <section className="best-psychol-card">
            <div className="overlap">
              <p className="best-match">Найкращий збіг</p>
              <div className="psychol-info">
                <div className="psychol-img-container">
                  <img
                    className="psuychol-img"
                    src={bestMatch.photo}
                    alt={`Фото ${bestMatch.name}`}
                  />
                </div>
                <div className="psychol-details">
                  <h2 className="psychol-name">{bestMatch.name}</h2>
                  <p className="psychol-profession">{bestMatch.profession}</p>
                  <p className="psychol-text">{bestMatch.bio}</p>
                  <button className="write-button">
                    <div className="div-wrapper">
                      <span className="text-wrapper-3">Написати</span>
                    </div>
                  </button>
                </div>
              </div>
            </div>
          </section>
        )}

        {others.map((t) => (
          <section key={t.id} className="view">
            <div className="overlap-2">
              <div className="psychol-info">
                <div className="psychol-img-container">
                  <img
                    className="psychol-img"
                    src={t.photo}
                    alt={`Фото ${t.name}`}
                  />
                </div>
                <div className="psychol-details">
                  <h2 className="psychol-name-2">{t.name}</h2>
                  <p className="psychol-profession-2">{t.profession}</p>
                  <p className="psychol-text">{t.bio}</p>
                  <button className="overlap-group-wrapper">
                    <div className="overlap-group-2">
                      <span className="text-wrapper-4">Написати</span>
                    </div>
                  </button>
                </div>
              </div>
            </div>
          </section>
        ))}
      </main>
    </div>
  );
}
