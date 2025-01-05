import { API } from "./api";

const API_URL = API;

export const fetchProductionIndex = async (query) => {
  const response = await API_URL.get('/production', {
    params: { query },
  });
  return response.data;
};

export const fetchProductionByYear = async (query) => {
    const response = await API_URL.get('/production', {
      params: { year: query },
    });
    return response.data;
  };
  