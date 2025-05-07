// src/pages/Test.jsx
import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { getQuestions, submitTest } from '../services/api';

export default function Test() {
  const navigate = useNavigate();
  const { firstName } = useLocation().state || {};

  const [questions, setQuestions] = useState([]);
  const [currentQuestionIdx, setCurrentQuestionIdx] = useState(0);
  const [answers, setAnswers] = useState({}); // { [questionId]: answerNumber }
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchQuestions() {
      try {
        const data = await getQuestions();
        setQuestions(data);
      } catch (e) {
        setError('Не вдалося завантажити питання');
      } finally {
        setLoading(false);
      }
    }
    fetchQuestions();
  }, []);

  const handleOptionClick = (optionIdx) => {
    const questionId = questions[currentQuestionIdx].id;
    setAnswers(prev => ({ ...prev, [questionId]: optionIdx + 1 }));
  };

  const nextQuestion = async () => {
    if (currentQuestionIdx < questions.length - 1) {
      setCurrentQuestionIdx(idx => idx + 1);
    } else {
      try {
        // prepare payload: [{ id, answer }]
        const payload = questions.map(q => ({ id: q.id, answer: answers[q.id] || null }));
        await submitTest(payload);
        navigate('/therapists');
      } catch (e) {
        alert('Помилка надсилання тесту');
      }
    }
  };

  const prevQuestion = () => {
    if (currentQuestionIdx > 0) {
      setCurrentQuestionIdx(idx => idx - 1);
    }
  };

  if (loading) return <p>Завантаження питань...</p>;
  if (error) return <p>{error}</p>;

  const question = questions[currentQuestionIdx];
  const selectedAnswer = answers[question.id];

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Привіт, {firstName || 'користувачу'}!</h2>
        <p style={{ marginBottom: '15px' }}>{question.title}</p>

        <div className="options">
          {question.options.map((opt, idx) => (
            <div
              key={idx}
              className={`option ${selectedAnswer === idx + 1 ? 'selected' : ''}`}
              onClick={() => handleOptionClick(idx)}
            >
              {opt}
            </div>
          ))}
        </div>

        <div className="buttons">
          <button className="button back" onClick={prevQuestion} disabled={currentQuestionIdx === 0}>
            Назад
          </button>
          <button className="button next" onClick={nextQuestion} disabled={selectedAnswer == null}>
            {currentQuestionIdx === questions.length - 1 ? 'Завершити' : 'Далі'}
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
