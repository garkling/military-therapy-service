// src/components/ChatList.js
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useApi } from "../api/apiClient.ts";           // ← helper that adds the token
import "./ChatList.css";

const ChatList = () => {
  const { listChats } = useApi();            // GET /api/v1/chats
  const [chats, setChats] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  /* ─────────────────────────────────────────────────────────
     fetch chats once on mount
  ───────────────────────────────────────────────────────── */
  useEffect(() => {
    const fetchChats = async () => {
      try {
        const data = await listChats();
        setChats(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchChats();
  }, [listChats]);

  /* ─────────────────────────────────────────────────────────
     rendering helpers
  ───────────────────────────────────────────────────────── */
  const renderLastLine = (chat) => {
    if (!chat.last_message) return "Немає повідомлень";
    return `${chat.last_message.author_name}: ${chat.last_message.content}`;
  };

  const renderTime = (iso) =>
    new Date(iso).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

  /* ───────────────────────────────────────────────────────── */
  if (loading) return <div className="chat-wrapper">Завантаження чатів…</div>;
  if (error)   return <div className="chat-wrapper">Помилка: {error}</div>;

  return (
    <div className="chat-wrapper">
      {/* ───────── sidebar ───────── */}
      <aside className="sidebar">
        <div className="overlap-group">
          <h1 className="platform-name">phoenix</h1>
          <nav className="nav">
            <ul>
              <li><Link to="/therapists" className="text-wrapper">психологи</Link></li>
              <li><Link to="/chats"      className="div">чати</Link></li>
              <li><Link to="/profile"    className="text-wrapper-2">профіль</Link></li>
            </ul>
          </nav>
        </div>
      </aside>

      {/* ───────── main list ───────── */}
      <main className="chat-container">
        <header className="chat-header">
          <h2 className="chat-title">Ваші чати</h2>
        </header>

        <ul className="chat-list">
          {chats.map((chat) => {
            const { id, participant } = chat;
            const name =
              [participant.first_name, participant.last_name]
                .filter(Boolean)
                .join(" ")
                || "Без імені";

            return (
              <li key={id} className="chat-preview">
                <Link to={`/chat/${id}`} className="chat-preview-link">
                  <div className="chat-preview-header">
                    <span className="chat-preview-name">{name}</span>
                    {chat.last_updated_at && (
                      <span className="chat-preview-time">
                        {renderTime(chat.last_updated_at)}
                      </span>
                    )}
                  </div>

                  <div className="chat-preview-last">
                    {renderLastLine(chat)}
                  </div>
                </Link>
              </li>
            );
          })}
        </ul>
      </main>
    </div>
  );
};

export default ChatList;
