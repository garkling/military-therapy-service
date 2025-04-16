// src/pages/Test.jsx
import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const questions = [
  {
    title: "Відчуття небезпеки",
    options: [
      "Рідко або ніколи",
      "Часом відчуваю тривогу",
      "Постійно насторожений і не можу розслабитися",
    ],
  },
  {
    title: "Гнів та самоконтроль",
    options: [
      "Ні, я контролюю свої емоції",
      "Іноді важко стриматися, але справляюся",
      "Часто вибухаю або не можу контролювати гнів",
    ],
  },
  {
    title: "Відносини з оточенням",
    options: [
      "Добре, є підтримка",
      "Часом важко, уникаю розмов про службу",
      "Віддалився від усіх, не хочу спілкуватися",
    ],
  },
  {
    title: "Спогади про бойові дії",
    options: [
      "Рідко або не заважають",
      "Іноді з'являються, але я можу контролювати їх",
      "Часто переслідують, важко від них позбутися",
    ],
  },
  {
    title: "Сон",
    options: [
      "Сплю нормально",
      "Часом прокидаюся або довго засинаю",
      "Постійно не висипаюся, сняться важкі сни або кошмари",
    ],
  },
  {
    title: "Відчуття сенсу та мотивація",
    options: [
      "Так, у мене є цілі та мотивація",
      "Часом втрачаю інтерес, але намагаюся триматися",
      "Важко знайти сенс у тому, що роблю",
    ],
  },
  {
    title: "Як я хочу відвідувати терапію?",
    options: ["Офлайн", "Онлайн"],
  },
  {
    title: "Терапевт якої статі буде комфортний для мене?",
    options: ["Чоловік", "Жінка", "Неважливо"],
  },
];

export default function Test() {
  const navigate = useNavigate();
  const location = useLocation();
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState([]);
  // Отримуємо firstName з location.state, якщо воно передано
  const firstName = location.state?.firstName || "";

  const handleOptionClick = (option) => {
    const updatedAnswers = [...answers];
    updatedAnswers[currentQuestion] = option;
    setAnswers(updatedAnswers);
  };

  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      console.log("Відповіді:", answers);
      // Після проходження всіх питань переходимо на сторінку з терапевтами
      navigate("/therapists");
    }
  };

  const prevQuestion = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Привіт, {firstName || "користувачу"}!</h2>
        <p style={{ marginBottom: "15px" }}>
          {questions[currentQuestion].title}
        </p>

        <div className="options">
          {questions[currentQuestion].options.map((option, index) => (
            <div
              key={index}
              className={`option ${
                answers[currentQuestion] === option ? "selected" : ""
              }`}
              onClick={() => handleOptionClick(option)}
            >
              {option}
            </div>
          ))}
        </div>

        <div className="buttons">
          <button className="button back" onClick={prevQuestion}>
            Назад
          </button>
          <button className="button next" onClick={nextQuestion}>
            {currentQuestion === questions.length - 1 ? "Завершити" : "Далі"}
          </button>
        </div>
      </div>

      <style jsx>{`
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #FFF9F2;
            padding: 20px;
          }
        .form-box {
          background: white;
          padding: 20px;
          border-radius: 10px;
          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          max-width: 400px;
          width: 100%;
        }
        .options {
          margin-top: 20px;
        }
        .option {
          background: #eaeec6;
          padding: 12px 16px;
          border-radius: 8px;
          margin: 10px 0;
          cursor: pointer;
          transition: all 0.2s ease;
        }
        .option:hover {
          background: #dbe2b9;
        }
        .option.selected {
          background: #c4dca6;
          font-weight: bold;
        }
        .buttons {
          display: flex;
          justify-content: space-between;
          margin-top: 20px;
        }
        .button {
          padding: 10px 20px;
          border: none;
          border-radius: 5px;
          font-size: 16px;
          cursor: pointer;
        }
        .back {
          background-color: #b6d6f2;
          color: #333;
        }
        .next {
          background-color: #aab08f;
          color: white;
        }
      `}</style>
    </div>
  );
}
