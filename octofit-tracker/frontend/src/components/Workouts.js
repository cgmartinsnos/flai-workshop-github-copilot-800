import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Workouts - Fetching from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Workouts - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2>💪 Workout Suggestions</h2>
          <p className="text-muted mb-0">Personalized workout recommendations</p>
        </div>
        <span className="badge bg-primary fs-6">{workouts.length} Workouts</span>
      </div>
      
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle me-2"></i>
          No workout suggestions available. Check back soon!
        </div>
      ) : (
        <div className="row g-4">
          {workouts.map((workout) => {
            // Difficulty badge color
            let difficultyClass = 'bg-secondary';
            if (workout.difficulty?.toLowerCase() === 'easy') difficultyClass = 'bg-success';
            else if (workout.difficulty?.toLowerCase() === 'medium') difficultyClass = 'bg-warning text-dark';
            else if (workout.difficulty?.toLowerCase() === 'hard') difficultyClass = 'bg-danger';
            
            return (
              <div key={workout.id} className="col-md-6 col-lg-4">
                <div className="card h-100">
                  <div className="card-header bg-info text-white">
                    <h5 className="mb-0">{workout.name || workout.title}</h5>
                    {(workout.user_name || workout.user) && (
                      <small className="d-block mt-1">
                        👤 For: {workout.user_name || workout.user}
                      </small>
                    )}
                  </div>
                  <div className="card-body">
                    <div className="mb-3">
                      <span className="badge bg-primary me-2">{workout.workout_type || workout.type || 'N/A'}</span>
                      <span className={`badge ${difficultyClass}`}>{workout.difficulty || 'N/A'}</span>
                    </div>
                    <p className="card-text">
                      {workout.description || <em className="text-muted">No description available</em>}
                    </p>
                    <hr />
                    <div className="d-flex justify-content-between mb-2">
                      <span><strong>⏱️ Duration:</strong></span>
                      <span className="badge bg-secondary">{workout.duration || 'N/A'} min</span>
                    </div>
                    {workout.calories_estimate && (
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>🔥 Calories:</strong></span>
                        <span className="badge bg-success">{workout.calories_estimate} cal</span>
                      </div>
                    )}
                    {(workout.target_muscle_group || workout.target_muscles) && (
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>🎯 Target:</strong></span>
                        <span className="badge bg-warning text-dark">{workout.target_muscle_group || workout.target_muscles}</span>
                      </div>
                    )}
                    {(workout.equipment_needed || workout.equipment) && (
                      <div className="d-flex justify-content-between mb-2">
                        <span><strong>🏋️ Equipment:</strong></span>
                        <span className="badge bg-secondary">{workout.equipment_needed || workout.equipment}</span>
                      </div>
                    )}
                    {(workout.created_at || workout.date) && (
                      <div className="text-muted small mt-2">
                        Created: {new Date(workout.created_at || workout.date).toLocaleDateString()}
                      </div>
                    )}
                  </div>
                  <div className="card-footer bg-transparent">
                    <button className="btn btn-sm btn-info text-white w-100">
                      Start Workout
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default Workouts;
