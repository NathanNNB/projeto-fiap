/* eslint-disable react/prop-types */

const JsonTable = ({ data }) => {
  let parsedData;

  try {
    // Parseia o campo `message` se existir e for uma string JSON
    parsedData = JSON.parse(data.message.replace(/'/g, '"')); // Substitui aspas simples por duplas e parseia
  } catch{
    return (
      <div className="error-message">
        Erro ao processar os dados fornecidos.{data.message}.
      </div>
    );
  }

  // Verifica se o resultado parseado é um array de objetos
  if (!Array.isArray(parsedData) || !parsedData.every((item) => typeof item === "object")) {
    return (
      <div className="error-message">
        Serviço indisponível: {data.message}.
      </div>
    );
  }

  return (
    <div className="json-table-container">
      <table>
        <thead>
          <tr>
            {/* Usa as chaves do primeiro objeto como cabeçalhos da tabela */}
            {Object.keys(parsedData[0]).map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {/* Itera sobre o array para criar as linhas da tabela */}
          {parsedData.map((item, index) => (
            <tr key={index}>
              {Object.values(item).map((value, i) => (
                <td key={i}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default JsonTable;