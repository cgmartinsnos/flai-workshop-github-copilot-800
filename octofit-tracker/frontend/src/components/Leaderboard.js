import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
        console.log('Leaderboard - Fetching from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Leaderboard - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2>🏆 Leaderboard</h2>
          <p className="text-muted mb-0">Top performers across all teams</p>
        </div>
      </div>
      
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle me-2"></i>
          No leaderboard data available yet.
        </div>
      ) : (
        <div className="row g-4">
          {leaderboard.map((entry, index) => {
            // Determine rank styling
            let rankClass = 'bg-secondary';
            let medalEmoji = '';
            if (index === 0) {
              rankClass = 'bg-warning text-dark';
              medalEmoji = '🥇';
            } else if (index === 1) {
              rankClass = 'bg-light text-dark';
              medalEmoji = '🥈';
            } else if (index === 2) {
              rankClass = 'bg-danger';
              medalEmoji = '🥉';
            }
            
            return (
              <div key={entry.id || index} className="col-md-6 col-lg-4">
                <div className="card h-100">
                  <div className={`card-header ${rankClass} text-white`}>
                    <h5 className="mb-0 d-flex justify-content-between align-items-center">
                      <span>{medalEmoji} #{index + 1}</span>
                      <span className="badge bg-dark">{entry.total_points || entry.points || 0} pts</span>
                    </h5>
                  </div>
                  <div className="card-body">
                    <h6 className="card-title">{entry.user_name || entry.user}</h6>
                    <hr />
                    <div className="d-flex justify-content-between mb-2">
                      <span className="text-muted">Team:</span>
                      <span className="badge bg-success">{entry.team_name || entry.team || 'N/A'}</span>
                    </div>
                    <div className="d-flex justify-content-between">
                      <span className="text-muted">Activities:</span>
                      <span className="badge bg-info text-dark">{entry.activity_count || entry.activities || 0}</span>
                    </div>
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

export default Leaderboard;
