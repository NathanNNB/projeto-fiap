/* eslint-disable react/prop-types */
// src/components/Section.jsx
import { useState } from "react";

const Section = ({ title, placeholder, handler }) => {
  const [inputValue, setInputValue] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleClick = async () => {
    setError(null);
    setResult(null);
    try {
      const data = await handler(inputValue);
      setResult(data);
    } catch {
      setError("Erro ao consultar a API.");
    }
  };

  return (
    <div className="section">
      <h2>{title}</h2>
      <input
        type="text"
        placeholder={placeholder}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <button onClick={handleClick}>Buscar</button>
      {error && <div className="message error">{error}</div>}
      {result && (
        <div className="message success">
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Section;
