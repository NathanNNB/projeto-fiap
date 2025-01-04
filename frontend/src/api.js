import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', 
});

export const fetchHello = async (query) => {
  const response = await API.get('/hello', {
    params: { query },
  });
  return response.data;
};

export const sendData = async (data) => {
  const response = await API.post('/data', data);
  return response.data;
};