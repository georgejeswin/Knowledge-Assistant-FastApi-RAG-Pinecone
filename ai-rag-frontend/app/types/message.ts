export type Role = "user" | "assistant";

export interface Message {
  id?: number;
  content: string;
  user_id: number;
  role: Role;
}