import { API } from "./api";

const API_URL = API;

export const fetchExportsIndex = async (query) => {
  const response = await API_URL.get('/exports', {
    params: { query },
  });
  return response.data;
};

export const fetchExportsByYear = async (query) => {
    const response = await API_URL.get('/exports', {
      params: { query },
    });
    return response.data;
  };
  