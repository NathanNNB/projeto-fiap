
import { useState } from 'react';
import {fetchProductionByYear} from './services/production'
import './App.css'; 

const App = () => {
  const [inputValue, setInputValue] = useState('');

  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFetchProduction = async () => {
    setError(null);
    try {
      const data = await fetchProductionByYear(inputValue);
      setResult(data);
    } catch {
      setError('Erro ao consultar a API.');
    }
  };

  return (
    <div className="container">
      <h1>Consulta aos dados da Embrapa</h1>
      
      <input
        type="text"
        placeholder="Digite algo..."
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />

      <button onClick={handleFetchProduction}>Buscar ano de produção (GET)</button>

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
