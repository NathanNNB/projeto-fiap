import { API } from "./api";

const API_URL = API;

export const fetchProductionByYear = async (query) => {

    const response = await API_URL.get('/production', {
      params: query,
    });
    return response.data;
  };
  