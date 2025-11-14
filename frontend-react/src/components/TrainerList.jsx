import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { trainerAPI } from '../services/api';
import './TrainerList.css';

const TrainerList = () => {
  const [trainers, setTrainers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [department, setDepartment] = useState('');
  const [specialization, setSpecialization] = useState('');
  const [choices, setChoices] = useState({ departments: [], specializations: [] });

  useEffect(() => {
    fetchChoices();
    fetchTrainers();
  }, [searchQuery, department, specialization]);

  const fetchChoices = async () => {
    try {
      const response = await trainerAPI.getChoices();
      setChoices(response.data);
    } catch (err) {
      console.error('Error fetching choices:', err);
    }
  };

  const fetchTrainers = async () => {
    try {
      setLoading(true);
      const params = {};
      if (searchQuery) params.search = searchQuery;
      if (department) params.department = department;
      if (specialization) params.specialization = specialization;

      const response = await trainerAPI.getAll(params);
      setTrainers(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load trainers. Make sure the Django server is running.');
      console.error('Error fetching trainers:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();
    fetchTrainers();
  };

  const handleClear = () => {
    setSearchQuery('');
    setDepartment('');
    setSpecialization('');
  };

  if (loading && trainers.length === 0) {
    return (
      <div className="content">
        <div className="loading">Loading trainers...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="content">
        <div className="error">{error}</div>
      </div>
    );
  }

  return (
    <div className="content">
      <h2 className="page-title">Search Trainers</h2>

      <div className="search-section">
        <form onSubmit={handleSearch} className="search-form">
          <div className="form-group">
            <label htmlFor="search">Search by Name or Email</label>
            <input
              type="text"
              id="search"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Enter name or email..."
            />
          </div>

          <div className="form-group">
            <label htmlFor="department">Department</label>
            <select
              id="department"
              value={department}
              onChange={(e) => setDepartment(e.target.value)}
            >
              <option value="">All Departments</option>
              {choices.departments.map((dept) => (
                <option key={dept.value} value={dept.value}>
                  {dept.label}
                </option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="specialization">Specialization</label>
            <select
              id="specialization"
              value={specialization}
              onChange={(e) => setSpecialization(e.target.value)}
            >
              <option value="">All Specializations</option>
              {choices.specializations.map((spec) => (
                <option key={spec.value} value={spec.value}>
                  {spec.label}
                </option>
              ))}
            </select>
          </div>

          <div className="form-group button-group">
            <button type="submit" className="btn btn-primary">
              Search
            </button>
            <button type="button" onClick={handleClear} className="btn btn-secondary">
              Clear
            </button>
          </div>
        </form>
      </div>

      {(searchQuery || department || specialization) && (
        <div className="results-info">
          <strong>Search Results:</strong> Found {trainers.length} trainer(s)
          {searchQuery && ` matching "${searchQuery}"`}
        </div>
      )}

      <div className="trainer-grid">
        {trainers.length > 0 ? (
          trainers.map((trainer) => (
            <div key={trainer.id} className="trainer-card">
              <div className="trainer-header">
                <div>
                  <div className="trainer-name">{trainer.full_name}</div>
                  <div className="trainer-email">{trainer.email}</div>
                </div>
                <span className="badge badge-department">
                  {trainer.department_display}
                </span>
              </div>

              <div className="trainer-info">
                <div className="info-row">
                  <span className="info-label">Specialization:</span>
                  <span className="info-value">{trainer.specialization_display}</span>
                </div>
                <div className="info-row">
                  <span className="info-label">Experience:</span>
                  <span className="info-value">{trainer.years_of_experience} years</span>
                </div>
              </div>

              <Link to={`/trainers/${trainer.id}`} className="view-details">
                View Details →
              </Link>
            </div>
          ))
        ) : (
          <div className="no-results">
            <h3>No trainers found</h3>
            <p>Try adjusting your search criteria</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default TrainerList;
