import { useState } from "react";
import Header from "./components/header.jsx";
import UrlForm from "./components/urlform.jsx";
import ResultCard from "./components/resultcard.jsx";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleAudit() {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://localhost:8000/audit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail);
      }

      setResult(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <Header />
      <UrlForm  url={url} setUrl={setUrl} handleAudit={handleAudit} loading={loading} />
      {error && <p className="error">{error}</p>}
      {result ? (
        <ResultCard result={result} />
      ) : (
        <div className="empty-state">
          <h3>Ready to Audit 🚀</h3>
          <p>Enter a website URL above and click <strong>Audit</strong> to analyze it.</p>
        </div>
      )}
      <footer className="footer">
      Built with ❤️ using React + FastAPI
      </footer>
    </div>
  );
}

export default App;