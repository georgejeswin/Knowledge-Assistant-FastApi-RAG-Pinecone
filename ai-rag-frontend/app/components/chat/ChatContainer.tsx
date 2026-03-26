'use client';

import { useEffect, useState, useRef } from "react";
import { Message } from "../../types/message";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import styles from "./chat.module.css";

export default function ChatContainer() {
  const [messages, setMessages] = useState<Message[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const fetchMessages = async () => {
    const token = localStorage.getItem("token");

    const res = await fetch("http://127.0.0.1:8000/api/v1/chat", {
      headers: { Authorization: `Bearer ${token}` },
    });

    const data = await res.json();
    setMessages(data);
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    fetchMessages();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);


  const sendMessage = async (input: string) => {
    const token = localStorage.getItem("token");

    // ✅ Add user message immediately
    const userMessage: Message = {
      id: Date.now(),
      content: input,
      user_id: 1,
      role: "user",
    };

    // placeholder assistant message
    const assistantMessage: Message = {
      id: Date.now() + 1,
      content: "",
      user_id: 1,
      role: "assistant",
    };

    setMessages((prev) => [...prev, userMessage, assistantMessage]);

    const res = await fetch("http://127.0.0.1:8000/api/v1/chat", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: input }),
    });

    const reader = res.body?.getReader();
    const decoder = new TextDecoder();

    let result = "";

    while (true) {
      const { done, value } = await reader!.read();
      if (done) break;

      result += decoder.decode(value);

      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          ...assistantMessage,
          content: result,
        };
        return updated;
      });
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.messages}>
        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} />
        ))}
        <div ref={messagesEndRef} />
      </div>

      <ChatInput onSend={sendMessage} />
    </div>
  );
}