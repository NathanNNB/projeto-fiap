import { API } from "./api";

const API_URL = API;

export const fetchProcessingIndex = async (query) => {
  const response = await API_URL.get('/processing', {
    params: { query },
  });
  return response.data;
};

export const fetchProcessingByYear = async (query) => {
    const response = await API_URL.get('/processing', {
      params: { query },
    });
    return response.data;
  };
  