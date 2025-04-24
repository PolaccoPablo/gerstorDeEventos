import axios from 'axios';

const API_URL = 'http://localhost:5000/events';

export const getEvents = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const createEvent = async (event) => {
  const response = await axios.post(API_URL, event);
  return response.data;
};