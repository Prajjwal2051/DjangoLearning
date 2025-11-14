import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { trainerAPI } from '../services/api';
import './TrainerDetail.css';

const TrainerDetail = () => {
  const { id } = useParams();
  const [trainer, setTrainer] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTrainer();
  }, [id]);

  const fetchTrainer = async () => {
    try {
      setLoading(true);
      const response = await trainerAPI.getById(id);
      setTrainer(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to load trainer details. Make sure the Django server is running.');
      console.error('Error fetching trainer:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="content">
        <div className="loading">Loading trainer details...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="content">
        <div className="error">{error}</div>
        <Link to="/trainers" className="back-link">
          ← Back to Trainer List
        </Link>
      </div>
    );
  }

  if (!trainer) {
    return (
      <div className="content">
        <div className="error">Trainer not found</div>
        <Link to="/trainers" className="back-link">
          ← Back to Trainer List
        </Link>
      </div>
    );
  }

  return (
    <div className="content">
      <Link to="/trainers" className="back-link">
        ← Back to Trainer List
      </Link>

      <div className="trainer-profile">
        <div className="profile-header">
          <div>
            <div className="profile-name">{trainer.full_name}</div>
            <div className="profile-email">{trainer.email}</div>
            {trainer.phone && (
              <div className="profile-email">📞 {trainer.phone}</div>
            )}
          </div>
          {trainer.is_active && <span className="status-badge">Active</span>}
        </div>
      </div>

      <div className="details-grid">
        <div className="detail-card">
          <h3>Professional Information</h3>
          <div className="detail-item">
            <span className="detail-label">Department:</span>
            <span className="detail-value">{trainer.department_display}</span>
          </div>
          <div className="detail-item">
            <span className="detail-label">Specialization:</span>
            <span className="detail-value">{trainer.specialization_display}</span>
          </div>
          <div className="detail-item">
            <span className="detail-label">Experience:</span>
            <span className="detail-value">{trainer.years_of_experience} years</span>
          </div>
        </div>

        <div className="detail-card">
          <h3>Timeline</h3>
          <div className="detail-item">
            <span className="detail-label">Joined Date:</span>
            <span className="detail-value">
              {new Date(trainer.joined_date).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}
            </span>
          </div>
          <div className="detail-item">
            <span className="detail-label">Profile Created:</span>
            <span className="detail-value">
              {new Date(trainer.created_at).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}
            </span>
          </div>
          <div className="detail-item">
            <span className="detail-label">Last Updated:</span>
            <span className="detail-value">
              {new Date(trainer.updated_at).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}
            </span>
          </div>
        </div>
      </div>

      <div className="bio-section">
        <h3>Biography</h3>
        {trainer.bio ? (
          <p className="bio-text">{trainer.bio}</p>
        ) : (
          <p className="no-bio">No biography available.</p>
        )}
      </div>
    </div>
  );
};

export default TrainerDetail;
