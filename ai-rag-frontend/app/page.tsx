// import FileUpload from "./components/FileUpload";
import Login from "./login/page";
import "./globals.css";

export default function Home() {
  return (
    <div className="min-h-full flex flex-col">
      <Login />
      {/* <FileUpload /> */}
    </div>
  );
}
