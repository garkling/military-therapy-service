import React from "react";
import "./ChatBox.css";

const ChatBox = ({ text, handleTextChange, handleSendMessage }) => {
  return (
    <div className="input-container">
      <input
        type="text"
        value={text}
        onChange={handleTextChange}
        onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
        className="input"
        placeholder="Введіть повідомлення"
      />
      <button className="send-button" onClick={handleSendMessage}>
        ➤
      </button>
    </div>
  );
};

export default ChatBox;
