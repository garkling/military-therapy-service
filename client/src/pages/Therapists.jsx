import React from "react";
import { Link } from "react-router-dom";
import "../styles/therapists.css";

const Therapists = () => {
  return (
    <div className="therapists">
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

      <main>
        {/* Тетяна */}
        <section className="best-psychol-card">
          <div className="overlap">
            <p className="best-match">Найкращий збіг</p>
            <div className="psychol-info">
              <div className="psychol-img-container">
                <img
                  className="psuychol-img"
                  src="https://c.animaapp.com/m8of8lb90J94Ha/img/psuychol-img.png"
                  alt="Фото Тетяни"
                />
              </div>
              <div className="psychol-details">
                <h2 className="psychol-name">Тетяна</h2>
                <p className="psychol-profession">психотерапевт</p>
                <p className="psychol-text">
                  Я допомагаю людям впоратися з тривогою, депресією та стресом.
                  Моя мета — створити безпечний простір, де ви зможете відкрито
                  говорити про свої почуття та проблеми.
                </p>
                <button className="write-button">
                  <div className="div-wrapper">
                    <span className="text-wrapper-3">Написати</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </section>
        <section className="view">
          <div className="overlap-2">
            <div className="psychol-info">
              <div className="psychol-img-container">
                <img
                  className="psychol-img"
                  src="https://c.animaapp.com/m8of8lb90J94Ha/img/psychol-img.png"
                  alt="Фото Марії"
                />
              </div>
              <div className="psychol-details">
                <h2 className="psychol-name-2">Марія</h2>
                <p className="psychol-profession-2">психолог</p>
                <p className="psychol-text">
                  Я військова психологиня. Допомагаю військовослужбовцям та ветеранам
                  справлятися з наслідками бойового досвіду, стресом і тривогою. У
                  роботі поєдную професійний підхід з емпатією.
                </p>
                <button className="overlap-group-wrapper">
                  <div className="overlap-group-2">
                    <span className="text-wrapper-4">Написати</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </section>
        <section className="view">
          <div className="overlap-2">
            <div className="psychol-info">
              <div className="psychol-img-container">
                <img
                  className="psychol-img"
                  src="https://www.fda.gov/files/styles/main_image_1/public/iStock-1413764595.jpg?itok=R8P2hM8Z"
                  alt="Фото Ольги"
                />
              </div>
              <div className="psychol-details">
                <h2 className="psychol-name-2">Ольга</h2>
                <p className="psychol-profession-2">психолог</p>
                <p className="psychol-text">
                  Я військова психологиня. Допомагаю військовослужбовцям та ветеранам
                  справлятися з наслідками бойового досвіду, стресом і тривогою. У
                  роботі поєдную професійний підхід з емпатією.
                </p>
                <button className="overlap-group-wrapper">
                  <div className="overlap-group-2">
                    <span className="text-wrapper-4">Написати</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </section>

        {/* Анна */}
        <section className="view">
          <div className="overlap-2">
            <div className="psychol-info">
              <div className="psychol-img-container">
                <img
                  className="psychol-img"
                  src="https://www.bellanaija.com/wp-content/uploads/2023/06/cropped-Financial-Jennifer-C.jpg"
                  alt="Фото Анни"
                />
              </div>
              <div className="psychol-details">
                <h2 className="psychol-name-2">Анна</h2>
                <p className="psychol-profession-2">психотерапевт</p>
                <p className="psychol-text">
                  Я військова психологиня. Допомагаю військовим справлятися з наслідками
                  бойового досвіду. Моя мета — підтримка, розуміння та зцілення.
                </p>
                <button className="overlap-group-wrapper">
                  <div className="overlap-group-2">
                    <span className="text-wrapper-4">Написати</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
};

export default Therapists;
