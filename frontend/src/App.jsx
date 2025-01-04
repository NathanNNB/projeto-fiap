
import { useState } from 'react';
import { fetchHello } from './api'; 
import './App.css'; 

const App = () => {
  const [inputValue, setInputValue] = useState('');

  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFetchHello = async () => {
    if (!inputValue.trim()) {
      setError('O campo não pode estar vazio.');
      setResult(null);
      return;
    }
    setError(null);
    try {
      const data = await fetchHello(inputValue);
      setResult(data);
    } catch {
      setError('Erro ao consultar a API.');
    }
  };

  return (
    <div className="container">
      <h1>Integração Flask + React</h1>
      
      <input
        type="text"
        placeholder="Digite algo..."
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />

      <button onClick={handleFetchHello}>Buscar Hello (GET)</button>

      {error && <div className="message error">{error}</div>}
      {result && (
        <div className="message success">
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default App;
