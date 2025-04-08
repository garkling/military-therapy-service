import React, { useState, useEffect, useRef } from 'react';
import './Chat.css';

const Chat = () => {
  const [messages, setMessages] = useState(() => {
    const storedMessages = localStorage.getItem('messages');
    return storedMessages ? JSON.parse(storedMessages) : [];
  });

  const [newMessage, setNewMessage] = useState('');
  const messagesEndRef = useRef(null);

  useEffect(() => {
    localStorage.setItem('messages', JSON.stringify(messages));
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = () => {
    if (newMessage.trim()) {
      const updatedMessages = [
        ...messages,
        {
          text: newMessage,
          sender: 'user',
          time: new Date().toLocaleTimeString().slice(0, 5),
        },
      ];
      setMessages(updatedMessages);
      setNewMessage('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="chat-wrapper">
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">phoenix</h1>
          <nav className="nav">
            <ul>
              <li><a href="#" className="text-wrapper">психологи</a></li>
              <li><a href="#" className="text-wrapper">чат</a></li>
              <li><a href="#" className="text-wrapper">профіль</a></li>
            </ul>
          </nav>
          <a href="tel:+380000000000" className="call-icon" aria-label="Зателефонувати">
            <img className="phone-call-img" src="https://c.animaapp.com/m8of8lb90J94Ha/img/phone-call-img.png" alt="Іконка телефону" />
          </a>
        </div>
      </aside>

      <main className="chat-container">
        <header className="chat-header">
          <button className="back-button">&lt; Назад</button>
          <h3 className="chat-title"><strong>Тетяна</strong></h3>
          <span className="status">онлайн</span>
        </header>

        <div className="messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              <div className="message-content">
                <p>{message.text}</p>
              </div>
              <span className="message-time">{message.time}</span>
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        <div className="input-container">
          <input
            type="text"
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Введіть ваше повідомлення"
          />
          <button onClick={handleSendMessage} className="send-button">&#9658;</button>
        </div>
      </main>
    </div>
  );
};

export default Chat;
