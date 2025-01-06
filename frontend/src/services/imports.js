import { API } from "./api";

const API_URL = API;

export const fetchImportsByYear = async (query) => {
    const response = await API_URL.get('/imports', {
      params: query ,
    });
    return response.data;
  };
  