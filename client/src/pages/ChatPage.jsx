// ChatPage.jsx
import React, { useState, useEffect } from "react";
import ChatList from "../components/ChatList";
import ChatBox from "../components/ChatBox";
import { useApi } from "../api/apiClient.ts";
import { useParams } from "react-router-dom";

const ChatPage = () => {
  const [text, setText] = useState("");
  const [messages, setMessages] = useState([]);

  const { chat_id } = useParams(); // Chat ID from URL params
  const { listMessages, sendMessage } = useApi();

  const currentUsername = "you"; // Ideally, fetch this dynamically

  useEffect(() => {
    if (!chat_id) return;

    const fetchMessages = async () => {
      const data = await listMessages(chat_id);
      setMessages(data);
    };

    fetchMessages();
  }, [chat_id, listMessages]);

  const handleSendMessage = async () => {
    if (!text.trim()) return;

    const newMessage = await sendMessage(chat_id, text);
    setMessages(prev => [...prev, newMessage]);
    setText("");
  };

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  return (
    <div className="chat-wrapper">
      <ChatList
        chats={messages.map(msg => ({
          username: msg.author_name,
          message: msg.content,
          time: new Date(msg.sent_at).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
        }))}
        users={[{ username: currentUsername }, { username: "companion" }]} // Adjust accordingly
        currentUsername={currentUsername}
        handleSendMessage={handleSendMessage}
      />
      <ChatBox
        text={text}
        handleTextChange={handleTextChange}
        handleSendMessage={handleSendMessage}
      />
    </div>
  );
};

export default ChatPage;
