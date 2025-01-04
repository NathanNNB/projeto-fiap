import { useState } from 'react';
import { fetchHello, sendData } from './api';

const App = () => {
  const [helloMessage, setHelloMessage] = useState('');
  const [postResponse, setPostResponse] = useState(null);

  const handleHello = async () => {
    try {
      const data = await fetchHello();
      setHelloMessage(data.message);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSendData = async () => {
    try {
      const dataToSend = { nome: 'Fulano', idade: 25 };
      const response = await sendData(dataToSend);
      setPostResponse(response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Integração Flask + React</h1>
      
      <button onClick={handleHello}>GET /api/hello</button>
      {helloMessage && <p>Resposta GET: {helloMessage}</p>}
      
      <button onClick={handleSendData}>POST /api/data</button>
      {postResponse && <pre>{JSON.stringify(postResponse, null, 2)}</pre>}
    </div>
  );
};

export default App;