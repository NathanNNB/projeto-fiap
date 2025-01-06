import { API } from "./api";

const API_URL = API;

export const fetchComerceByYear = async (query) => {
    const response = await API_URL.get('/comerce', {
      params: query ,
    });
    return response.data;
  };
  