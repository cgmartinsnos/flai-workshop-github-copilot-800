import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink, Link } from 'react-router-dom';
import './App.css';
import logo from './logo.png';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="container mt-5">
      <div className="jumbotron p-5 rounded">
        <h1 className="display-4">Welcome to OctoFit Tracker! 🏃‍♂️</h1>
        <p className="lead">
          Track your fitness activities, compete with your team, and achieve your health goals!
        </p>
        <hr className="my-4" style={{borderColor: 'rgba(255,255,255,0.3)'}} />
        <p className="mb-4">
          Use the navigation menu above to explore activities, view the leaderboard, 
          manage teams, check users, and get personalized workout suggestions.
        </p>
        <div className="row text-center mt-4">
          <div className="col-md-4 mb-3">
            <Link to="/activities" className="text-decoration-none">
              <div className="card bg-light clickable-card">
                <div className="card-body">
                  <h3>🏃‍♂️</h3>
                  <h5 className="card-title">Track Activities</h5>
                  <p className="card-text">Log your workouts and monitor your progress</p>
                </div>
              </div>
            </Link>
          </div>
          <div className="col-md-4 mb-3">
            <Link to="/leaderboard" className="text-decoration-none">
              <div className="card bg-light clickable-card">
                <div className="card-body">
                  <h3>🏆</h3>
                  <h5 className="card-title">Leaderboard</h5>
                  <p className="card-text">Challenge your team and climb the leaderboard</p>
                </div>
              </div>
            </Link>
          </div>
          <div className="col-md-4 mb-3">
            <Link to="/users" className="text-decoration-none">
              <div className="card bg-light clickable-card">
                <div className="card-body">
                  <h3>👥</h3>
                  <h5 className="card-title">Users</h5>
                  <p className="card-text">View and manage all registered users</p>
                </div>
              </div>
            </Link>
          </div>
          <div className="col-md-4 mb-3">
            <Link to="/teams" className="text-decoration-none">
              <div className="card bg-light clickable-card">
                <div className="card-body">
                  <h3>👥</h3>
                  <h5 className="card-title">Teams</h5>
                  <p className="card-text">Create and manage fitness teams</p>
                </div>
              </div>
            </Link>
          </div>
          <div className="col-md-4 mb-3">
            <Link to="/workouts" className="text-decoration-none">
              <div className="card bg-light clickable-card">
                <div className="card-body">
                  <h3>💪</h3>
                  <h5 className="card-title">Workout Suggestions</h5>
                  <p className="card-text">Get personalized workout recommendations</p>
                </div>
              </div>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <NavLink className="navbar-brand" to="/">
              <img src={logo} alt="OctoFit Logo" className="navbar-logo" />
              <span className="navbar-brand-text">OctoFit Tracker</span>
            </NavLink>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/"
                  >
                    Home
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/activities"
                  >
                    Activities
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/leaderboard"
                  >
                    Leaderboard
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/teams"
                  >
                    Teams
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/users"
                  >
                    Users
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/workouts"
                  >
                    Workouts
                  </NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
