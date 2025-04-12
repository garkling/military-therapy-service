import React, { useState } from "react";

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

export default function TherapyQuiz() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState([]);

  const handleOptionClick = (option) => {
    const updatedAnswers = [...answers];
    updatedAnswers[currentQuestion] = option;
    setAnswers(updatedAnswers);
  };

  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      alert("Дякуємо за проходження тесту!");
      console.log("Відповіді:", answers);
    }
  };

  const prevQuestion = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  return (
    <div className="container">
      <div className="progress-bar">
        {questions.map((_, index) => (
          <div
            key={index}
            className={`bar ${index <= currentQuestion ? "active" : ""}`}
          ></div>
        ))}
      </div>
      <h2>{questions[currentQuestion].title}</h2>
      <div className="options">
        {questions[currentQuestion].options.map((option, index) => (
          <div
            key={index}
            className={`option ${answers[currentQuestion] === option ? "selected" : ""}`}
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

      <style jsx>{`
        .container {
          background: #f9faef;
          padding: 20px;
          border-radius: 10px;
          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
          text-align: center;
          max-width: 400px;
          margin: auto;
        }
        .progress-bar {
          display: flex;
          justify-content: space-between;
          margin-bottom: 20px;
        }
        .bar {
          height: 5px;
          width: 12%;
          background: #dcdcdc;
          border-radius: 5px;
        }
        .bar.active {
          background: #c4d4a4;
        }
        h2 {
          color: #333;
          margin-bottom: 20px;
        }
        .option {
          background: #d1cd99;
          padding: 10px;
          border-radius: 5px;
          margin: 10px 0;
          cursor: pointer;
        }
        .option.selected {
          background: #b7ba80;
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
          cursor: pointer;
          font-size: 16px;
        }
        .back {
          background: #dcdcdc;
        }
        .next {
          background: #aab08f;
          color: white;
        }
      `}</style>
    </div>
  );
}
