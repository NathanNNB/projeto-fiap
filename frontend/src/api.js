import axios from 'axios';

// Base URL do Flask local:
const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
});

// Exemplo de requisição GET
export const fetchHello = async () => {
  const response = await API.get('/hello');
  return response.data;
};

// Exemplo de requisição POST
export const sendData = async (payload) => {
  const response = await API.post('/data', payload);
  return response.data;
};