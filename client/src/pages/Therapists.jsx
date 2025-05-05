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
      <aside>{/* ваше sidebar */}</aside>
      <main>
        {list.map(t => (
          <section key={t.id} className="view">
            <img src={t.photo} alt={`Фото ${t.name}`} />
            <h2>{t.name}</h2>
            <p>{t.profession}</p>
            <p>{t.bio}</p>
            <button>Написати</button>
          </section>
        ))}
      </main>
    </div>
  );
}
