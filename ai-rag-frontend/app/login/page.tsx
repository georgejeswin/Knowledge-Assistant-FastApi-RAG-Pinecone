"use client";

import { useState } from "react";
import API, { setAuthToken } from '../lib/api';

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const res = await API.post("/auth/login", { email, password });

    const token = res.data.access_token;
    localStorage.setItem("token", token);
    setAuthToken(token);

    window.location.href = "/chat";
  };

  return (
    <div>
      <h1>Login</h1>
      <input onChange={(e) => setEmail(e.target.value)} placeholder="email" />
      <input onChange={(e) => setPassword(e.target.value)} placeholder="password" type="password" />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}