import React, { useState } from "react";
import ChatList from "../components/ChatList";
import ChatBox from "../components/ChatBox";
import "../components/ChatList.css";
import "../components/ChatBox.css";

const ChatPage = () => {
  const [text, setText] = useState("");
  const [chats, setChats] = useState([]);
  const currentUsername = "you";

  const users = [
    { username: "you", name: "Я", online: true },
    { username: "companion", name: "Тетяна", online: true },
  ];

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleSendMessage = () => {
    if (!text.trim()) return;

    const newChat = {
      username: currentUsername,
      message: text,
      time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    };

    setChats((prev) => [...prev, newChat]);
    setText("");
  };

  return (
    <div className="chat-wrapper">
      <ChatList
        chats={chats}
        users={users}
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
