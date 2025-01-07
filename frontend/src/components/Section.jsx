/* eslint-disable react/prop-types */
import { useState } from "react";
import "./Section.css" ;
import JsonTable from "./JsonTable";
const Section = ({ title, inputs = [], handler }) => {
  const [formData, setFormData] = useState(
    inputs.reduce((acc, input) => ({ ...acc, [input.name]: "" }), {})
  );
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleClick = async () => {
    setError(null);
    setResult(null);
    try {
      const data = await handler(formData);
      setResult(data);
    } catch {
      setError("Erro ao consultar a API.");
    }
  };

  return (
    <div className="section">
      <h2>{title}</h2>
      {inputs.map((input) => (
        <div key={input.name} className="input-group">
          {input.type === "select" ? (
            <select
              name={input.name}
              value={formData[input.name]}
              onChange={handleInputChange}
            >
              <option value="">Selecione uma opção</option>
              {input.options.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          ) : (
            <input
              type={input.type || "text"}
              placeholder={input.placeholder}
              name={input.name}
              value={formData[input.name]}
              onChange={handleInputChange}
            />
          )}
        </div>
      ))}
      <button onClick={handleClick}>Buscar</button>
      {error && <div className="message error">{error}</div>}
      {result && (
        <div className="message success">
         <JsonTable data={result}/>
        </div>
      )}
    </div>
  );
};

export default Section;
