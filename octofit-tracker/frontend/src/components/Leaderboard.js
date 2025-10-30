import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard API endpoint:', apiUrl);
        console.log('Fetched leaderboard:', data);
        setLeaderboard(data.results ? data.results : data);
      });
  }, [apiUrl]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title text-primary mb-4">Leaderboard</h2>
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>Team</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry, idx) => (
              <tr key={idx}>
                <td>{entry.team && entry.team.name ? entry.team.name : 'Team'}</td>
                <td>{entry.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
