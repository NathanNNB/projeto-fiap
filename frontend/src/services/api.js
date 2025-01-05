import axios from 'axios';

export const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', 
});

export const fetchHello = async (query) => {
  const response = await API.get('/processing', {
    params: { year: query },
  });
  return response.data;
};