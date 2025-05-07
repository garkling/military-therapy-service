import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { submitTest } from '../services/api';

const questions = [
  {
    id: 1,
    title: "Чи відчуваєте ви, що у вашому житті стало складніше керувати стресом чи тривогою?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
  {
    id: 2,
    title: "Чи зазнаєте ви труднощів зі сном (важко заснути, часто прокидаєтесь, мучать кошмари)?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
  {
    id: 3,
    title: "Настільки часто у вас виникають нав’язливі або болісні спогади про військовий досвід?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
  {
    id: 4,
    title: "Наскільки часто ви відчуваєте емоційне виснаження або безнадійність?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
  {
    id: 5,
    title: "Чи є у вас відчуття, що вам складно ділитися переживаннями з близькими або фахівцями?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
  {
    id: 6,
    title: "Настільки часто у вас з’являються думки або відчуття провини, пов’язані з пережитими подіями (втратами, вчиненими діями тощо)?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
  {
    id: 7,
    title: "Наскільки вам важко виконувати буденні справи або функціонувати так, як ви хотіли б?",
    options: ["Ніколи", "Іноді", "Часто"],
  },
];

export default function Test() {
  const navigate = useNavigate();
  const { firstName } = useLocation().state || {};
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState(Array(questions.length).fill(null));

  const handleOptionClick = (optionIndex) => {
    const updated = [...answers];
    updated[currentQuestion] = optionIndex;
    setAnswers(updated);
  };

  const nextQuestion = async () => {
    if (currentQuestion < questions.length - 1) {
      return setCurrentQuestion((q) => q + 1);
    }

    try {
      const formattedAnswers = questions.map((q, index) => ({
        id: q.id,
        answer: answers[index],
      }));

      const therapists = await submitTest(formattedAnswers);
      navigate('/therapists', { state: { therapists, firstName } });
    } catch (error) {
      console.error(error);
      alert('Помилка надсилання тесту');
    }
  };

  const prevQuestion = () => {
    if (currentQuestion > 0) setCurrentQuestion((q) => q - 1);
  };

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Привіт, {firstName || 'користувачу'}!</h2>
        <p style={{ marginBottom: '15px' }}>
          {questions[currentQuestion].title}
        </p>

        <div className="options">
          {questions[currentQuestion].options.map((option, index) => (
            <div
              key={index}
              className={`option ${answers[currentQuestion] === index ? 'selected' : ''}`}
              onClick={() => handleOptionClick(index)}
            >
              {option}
            </div>
          ))}
        </div>

        <div className="buttons">
          <button className="button back" onClick={prevQuestion} disabled={currentQuestion === 0}>
            Назад
          </button>
          <button className="button next" onClick={nextQuestion}>
            {currentQuestion === questions.length - 1 ? 'Завершити' : 'Далі'}
          </button>
        </div>
      </div>

      <style jsx="true">{`
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
