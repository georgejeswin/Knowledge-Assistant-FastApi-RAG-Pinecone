"use client";

import { useState } from "react";
import { useRouter } from 'next/navigation';
import API from '../lib/api';
import styles from "./login.module.css"

export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e:React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();
    if(!email.length || !password.length) return;
    const res = await API.post("/auth/login", { email, password });

    const token = res.data.access_token;
    localStorage.setItem("token", token);
    // setAuthToken(token);

    router.replace("/chat")
  };

  return (
    <div className={styles.container}>
      <form className={styles.form} onSubmit={handleLogin}>
        <h1 className={styles.h1}>Login</h1>
        <input className={styles.input} onChange={(e) => setEmail(e.target.value)} placeholder="Enter your email" />
        <input className={styles.input} onChange={(e) => setPassword(e.target.value)} placeholder="Enter your password" type="password" />
        <button className={styles.button} type="submit">Login</button>
      </form>
    </div>
  );
}