import { useState } from "react";
import api from "../api.js";

function Home() {
  const [conversationId, setConversationId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  async function sendMessage(event) {
    event.preventDefault();

    const text = input.trim();

    if (!text || isLoading) {
      return;
    }

    setError("");

    const userMessage = {
      role: "user",
      content: text,
    };

    setMessages((previousMessages) => [...previousMessages, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await api.post("/api/chat", {
        message: text,
        conversation_id: conversationId,
      });

      setConversationId(response.data.conversation_id);

      const assistantMessage = {
        role: "assistant",
        content: response.data.answer,
      };

      setMessages((previousMessages) => [
        ...previousMessages,
        assistantMessage,
      ]);
    } catch (err) {
      console.error(err);

      setError(
        err.response?.data?.detail ||
          "Something went wrong. Please try again."
      );
    } finally {
      setIsLoading(false);
    }
  }

  function startNewChat() {
    setConversationId(null);
    setMessages([]);
    setInput("");
    setError("");
  }

  return (
    <section className="chat-page">
      <div className="chat-header">
        <div>
          <h2>What’s on the agenda today?</h2>
          <p>Start a conversation and continue it in the same context.</p>
        </div>

        <button className="new-chat-button" onClick={startNewChat}>
          New chat
        </button>
      </div>

      <div className="chat-box">
        {messages.length === 0 && (
          <div className="empty-state">
            <h3>Ask anything</h3>
            <p>For example: Tell me a one-liner programming joke.</p>
          </div>
        )}

        {messages.map((message, index) => (
          <div
            key={index}
            className={
              message.role === "user"
                ? "message-row user-row"
                : "message-row assistant-row"
            }
          >
            <div
              className={
                message.role === "user"
                  ? "message-bubble user-bubble"
                  : "message-bubble assistant-bubble"
              }
            >
              {message.content}
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="message-row assistant-row">
            <div className="message-bubble assistant-bubble loading">
              Thinking...
            </div>
          </div>
        )}
      </div>

      {error && <div className="error-box">{error}</div>}

      <form className="chat-form" onSubmit={sendMessage}>
        <input
          type="text"
          placeholder="Ask anything"
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />

        <button type="submit" disabled={isLoading}>
          Send
        </button>
      </form>
    </section>
  );
}

export default Home;