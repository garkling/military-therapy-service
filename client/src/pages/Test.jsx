// src/pages/Test.jsx
import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { submitTest } from '../services/api';

// Варіанти відповідей для всіх питань
const answerOptions = [
  "Ніколи", 
  "Зрідка", 
  "Іноді", 
  "Часто", 
  "Дуже часто"
];


const specialQuestions = {
  7: {
    options: ["Офлайн", "Онлайн"]
  },
  8: {
    options: ["Чоловік", "Жінка", "Неважливо"]
  }
};

export default function Test() {
  const navigate = useNavigate();
  const { firstName } = useLocation().state || {};
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {

    fetch('/entry_test.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch questions');
        }
        return response.json();
      })
      .then(data => {
        setQuestions(data.questions || []);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error loading questions:', err);
        setError('Не вдалося завантажити питання. Спробуйте пізніше.');
        setLoading(false);
      });
  }, []);

  const handleOptionClick = (questionId, optionIndex) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: optionIndex
    }));
  };

  const nextQuestion = async () => {
    if (currentQuestion < questions.length - 1) {
      return setCurrentQuestion(q => q + 1);
    }
    
    try {
      // Підготуємо формат відповідей для відправки на бекенд
      const formattedAnswers = Object.entries(answers).map(([questionId, answerIndex]) => ({
        questionId: parseInt(questionId),
        answer: answerIndex
      }));
      
      await submitTest(formattedAnswers);
      navigate('/therapists');
    } catch (error) {
      console.error('Error submitting test:', error);
      alert('Помилка надсилання тесту');
    }
  };

  const prevQuestion = () => {
    if (currentQuestion > 0) setCurrentQuestion(q => q - 1);
  };

  if (loading) {
    return (
      <div className="center-container">
        <div className="form-box">
          <p>Завантаження питань...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="center-container">
        <div className="form-box">
          <p>{error}</p>
          <button className="button next" onClick={() => window.location.reload()}>
            Спробувати знову
          </button>
        </div>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="center-container">
        <div className="form-box">
          <p>Питання не знайдено</p>
        </div>
      </div>
    );
  }

  const currentQuestionData = questions[currentQuestion];
  const currentQuestionId = currentQuestionData.id;
  

  const currentOptions = specialQuestions[currentQuestionId]?.options || answerOptions;

  return (
    <div className="center-container">
      <div className="form-box">
        <h2>Психологічна оцінка</h2>
        {firstName && <p>Привіт, {firstName}! Будь ласка, дайте відповідь на всі питання.</p>}
        
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
          ></div>
        </div>
        <p className="progress-text">
          Питання {currentQuestion + 1} з {questions.length}
        </p>
        
        <h3>{currentQuestionData.question}</h3>
        
        <div className="options">
          {currentOptions.map((option, index) => (
            <div
              key={index}
              className={`option ${answers[currentQuestionId] === index ? 'selected' : ''}`}
              onClick={() => handleOptionClick(currentQuestionId, index)}
            >
              {option}
            </div>
          ))}
        </div>
        
        <div className="buttons">
          <button 
            className="button back" 
            onClick={prevQuestion} 
            disabled={currentQuestion === 0}
            style={{ opacity: currentQuestion === 0 ? 0.5 : 1 }}
          >
            Назад
          </button>
          
          <button 
            className="button next" 
            onClick={nextQuestion}
            disabled={answers[currentQuestionId] === undefined}
            style={{ opacity: answers[currentQuestionId] === undefined ? 0.5 : 1 }}
          >
            {currentQuestion < questions.length - 1 ? 'Далі' : 'Завершити'}
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
          padding: 30px;
          border-radius: 10px;
          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          max-width: 500px;
          width: 100%;
        }
        .progress-bar {
          background: #f0f0f0;
          height: 10px;
          border-radius: 5px;
          margin: 20px 0 10px;
        }
        .progress-fill {
          background: #aab08f;
          height: 100%;
          border-radius: 5px;
          transition: width 0.3s ease;
        }
        .progress-text {
          margin-bottom: 20px;
          font-size: 14px;
          color: #666;
        }
        h3 {
          margin-bottom: 20px;
          font-size: 18px;
          line-height: 1.4;
        }
        .options {
          margin: 25px 0;
        }
        .option {
          background: #eaeec6;
          padding: 12px 16px;
          border-radius: 8px;
          margin: 10px 0;
          cursor: pointer;
          transition: all 0.2s ease;
          text-align: left;
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
          margin-top: 30px;
        }
        .button {
          padding: 12px 25px;
          border: none;
          border-radius: 5px;
          font-size: 16px;
          cursor: pointer;
          transition: all 0.2s ease;
        }
        .button:disabled {
          cursor: not-allowed;
        }
        .back {
          background-color: #b6d6f2;
          color: #333;
        }
        .back:hover:not(:disabled) {
          background-color: #9ac7ea;
        }
        .next {
          background-color: #aab08f;
          color: white;
        }
        .next:hover:not(:disabled) {
          background-color: #93a079;
        }
      `}</style>
    </div>
  );
}
