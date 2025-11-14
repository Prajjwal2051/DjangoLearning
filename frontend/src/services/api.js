import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Trainer API endpoints
export const trainerApi = {
  // Get all trainers with optional filters
  getTrainers: (params = {}) => {
    return api.get('/trainers/', { params });
  },

  // Get a single trainer by ID
  getTrainer: (id) => {
    return api.get(`/trainers/${id}/`);
  },

  // Create a new trainer
  createTrainer: (data) => {
    return api.post('/trainers/', data);
  },

  // Update a trainer
  updateTrainer: (id, data) => {
    return api.put(`/trainers/${id}/`, data);
  },

  // Partially update a trainer
  patchTrainer: (id, data) => {
    return api.patch(`/trainers/${id}/`, data);
  },

  // Delete a trainer
  deleteTrainer: (id) => {
    return api.delete(`/trainers/${id}/`);
  },

  // Get department and specialization choices
  getChoices: () => {
    return api.get('/trainers/choices/');
  },

  // Get trainer statistics
  getStats: () => {
    return api.get('/trainers/stats/');
  },
};

export default api;
