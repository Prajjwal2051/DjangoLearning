import axios from 'axios';

// Base URL for the Django API
const API_BASE_URL = 'http://127.0.0.1:8000/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Trainer API endpoints
export const trainerAPI = {
  // Get all trainers with optional filters
  getAll: (params = {}) => {
    return api.get('/trainers/', { params });
  },

  // Get a single trainer by ID
  getById: (id) => {
    return api.get(`/trainers/${id}/`);
  },

  // Get department and specialization choices
  getChoices: () => {
    return api.get('/trainers/choices/');
  },

  // Get trainer statistics
  getStats: () => {
    return api.get('/trainers/stats/');
  },

  // Create a new trainer
  create: (data) => {
    return api.post('/trainers/', data);
  },

  // Update a trainer
  update: (id, data) => {
    return api.put(`/trainers/${id}/`, data);
  },

  // Delete a trainer
  delete: (id) => {
    return api.delete(`/trainers/${id}/`);
  },
};

export default api;
