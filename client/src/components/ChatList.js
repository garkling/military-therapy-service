import React, { useState, useEffect, useRef } from "react";
import "./ChatList.css";
import { Link } from "react-router-dom";

const ChatList = ({ chats, users, currentUsername, handleSendMessage }) => {
  const [newMessage, setNewMessage] = useState("");
  const messagesEndRef = useRef(null);

  const companion = users.find(user => user.username !== currentUsername) || {};
  const companionName = companion.name || companion.username || "User";
  const isOnline = companion.online ? "онлайн" : "офлайн";

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chats]);

  const handleMessageSend = () => {
    if (newMessage.trim()) {
      handleSendMessage(newMessage);
      setNewMessage("");
    }
  };

  const handleTextChange = (e) => {
    setNewMessage(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleMessageSend();
    }
  };

  return (
    <div className="chat-wrapper">
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">phoenix</h1>
          <nav className="nav">
            <ul>
              <li><Link to="/therapists" className="text-wrapper">психологи</Link></li>
              <li><Link to="/chat" className="div">чат</Link></li>
              <li><Link to="/profile" className="text-wrapper-2">профіль</Link></li>
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
          <h3 className="chat-title"><strong>{companionName}</strong></h3>
          <span className={`status ${isOnline === 'онлайн' ? 'online' : 'offline'}`}>
            {isOnline}
          </span>
        </header>

        <div className="messages">
          {chats.map((chat, index) => {
            const isCurrentUser = chat.username === currentUsername;
            return (
              <div key={index} className={`message-row ${isCurrentUser ? 'own' : 'other'}`}>
                <div className="message-bubble">
                  <div className="message-text">{chat.message}</div>
                  <div className="message-time">{chat.time || "..."}</div>
                </div>
              </div>
            );
          })}
          <div ref={messagesEndRef} />
        </div>
      </main>
    </div>
  );
};

export default ChatList;