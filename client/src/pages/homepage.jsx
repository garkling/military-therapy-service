// src/pages/Homepage.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './homepage.css'; // підключаємо оновлений css

const Homepage = () => {
  return (
    <div className="full-background">
      {/* Верхня панель - зовнішній блок, що розтягується на всю ширину */}
      <header className="header">
        <nav className="nav">
          <div className="nav-left">
            <button className="burger">☰</button>
            <div className="logo">
              therapy<br />platform
            </div>
          </div>
          <div className="nav-right">
            <div className="menu">
              <a href="#">Психологи</a>
              <a href="#">Чат</a>
              <a href="#">Профіль</a>
            </div>
          </div>
        </nav>
      </header>

      {/* Основний блок із градієнтним фоном */}
      <div className="container">
        <div className="content">
          <div className="tagline">
            Психологічна підтримка для тих,<br />хто пройшов через війну
          </div>

          <div className="description">
            <strong>Повернення з війни</strong> — це ще один бій, який часто не видно ззовні.
            Ми створили цю платформу, щоб ви могли знайти фахівця, який дійсно знає, що таке травма, тиша після бою, ніч без сну. Тут немає формальностей чи осуду — лише допомога.
            <br />
            Безпечно. Конфіденційно. Професійно.
          </div>

          <div className="cta">
            <Link to="/login">
              <button>Обрати психотерапевта</button>
            </Link>
          </div>

          <div className="message">
            Ти не сам.<br />
            Допомога поруч.
          </div>
        </div>
      </div>
    </div>
  );
};

export default Homepage;
