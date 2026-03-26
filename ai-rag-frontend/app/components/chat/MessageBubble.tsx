import { Message } from "../../types/message";
import styles from "./chat.module.css";

export default function MessageBubble({ message }: { message: Message }) {
  return (
    <div
      className={
        message.role === "user"
          ? styles.userMessage
          : styles.assistantMessage
      }
    >
      {message.content}
    </div>
  );
}