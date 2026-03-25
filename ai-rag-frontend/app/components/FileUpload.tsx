"use client";

export default function FileUpload() {
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

    alert("Uploaded!");
  };

  return (
    <input
      type="file"
      onChange={(e) => uploadFile(e.target.files![0])}
    />
  );
}