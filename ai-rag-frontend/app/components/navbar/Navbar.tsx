'use client';
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

  const uploadFile = async (file: File) => {
    const token = localStorage.getItem("token");

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:8000/api/v1/document/upload", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });
    // formData.delete("file")
    alert("Uploaded!");
  };

  return (
    <div className={styles.container}>
      <h1>RAG Chat</h1>
      <div className={styles.buttons}>
        <input
          type="file"
          onChange={(e) => uploadFile(e.target.files![0])}
        />
        <button onClick={(e) => handleLogout(e)}>Logout</button>
      </div>
    </div>
  );
}