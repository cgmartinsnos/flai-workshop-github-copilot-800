import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
        console.log('Teams - Fetching from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Teams - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="container mt-4"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2>👥 Teams</h2>
          <p className="text-muted mb-0">Manage and view all fitness teams</p>
        </div>
        <span className="badge bg-primary fs-6">{teams.length} Teams</span>
      </div>
      
      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle me-2"></i>
          No teams found. Create your first team!
        </div>
      ) : (
        <div className="row g-4">
          {teams.map((team) => (
            <div key={team.id} className="col-md-6 col-lg-4">
              <div className="card h-100">
                <div className="card-header bg-success text-white">
                  <h5 className="mb-0 d-flex justify-content-between align-items-center">
                    <span>{team.name}</span>
                    <span className="badge bg-light text-dark">{team.member_count || team.members || 0} members</span>
                  </h5>
                </div>
                <div className="card-body">
                  <p className="card-text">
                    <strong>Description:</strong><br />
                    {team.description || <em className="text-muted">No description provided</em>}
                  </p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center">
                    <small className="text-muted">
                      Created: {team.created_at ? new Date(team.created_at).toLocaleDateString() : 'N/A'}
                    </small>
                  </div>
                </div>
                <div className="card-footer bg-transparent">
                  <button className="btn btn-sm btn-outline-success w-100">
                    View Team Details
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Teams;
