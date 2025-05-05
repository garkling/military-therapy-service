// src/pages/Homepage.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/homepage.css';

const Homepage = () => {
  return (
    <div className="full-background">
      <div className="header-panel">
        <div className="logo-container">
          <div className="logo">PHOENIX</div>
        </div>
      </div>
      
      <div className="content-wrapper">
        <div className="content">
          <div className="tagline">
            Психологічна підтримка для тих,<br />
            хто пройшов через війну
          </div>
          <div className="description">
            Повернення з війни — це ще один бій, який часто не видно зовні.<br />
             Ми створили цю платформу, щоб ви могли знайти фахівця,<br />
             який дійсно знає, що таке травма, тиша після бою, ніч без сну.<br />
             Тут немає формальностей чи осуду — лише допомога.<br />
            Безпечно. Конфіденційно. Професійно.
          </div>
          <div className="cta">
            <Link to="/login">
              <button>Обрати психотерапевта</button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Homepage;