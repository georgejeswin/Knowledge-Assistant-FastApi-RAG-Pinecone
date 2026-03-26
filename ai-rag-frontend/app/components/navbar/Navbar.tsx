'use client';

import { useEffect, useState } from "react";
// import { setAuthToken } from "@/app/lib/api";
import styles from "./navbar.module.css";
import { useRouter } from 'next/navigation';

export default function Navbar() {
  const router = useRouter();

  const handleLogout = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
    e.preventDefault();
    localStorage.removeItem("token");

    router.replace("/")
    router.refresh()
  }

  return (
    <div className={styles.container}>
      <h1>RAG Chat</h1>
      <button onClick={(e) => handleLogout(e)}>Logout</button>
    </div>
  );
}