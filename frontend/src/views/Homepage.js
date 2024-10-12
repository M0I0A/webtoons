import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';


function Homepage() {
  const [webtoons, setWebtoons] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:8000/api/webtoons/') // Update URL as needed
      .then(response => {
        setWebtoons(response.data);
      })
      .catch(error => {
        console.error('Error fetching the webtoons:', error);
      });
  }, []);



  return (
    <div>
      <>
  <main role="madin" style={{ marginTop: 50 }}>
    <div className="jumbotron">
      <div className="container">
        <h1 className="display-3">Top 10 Popular Webtoons with Over 50 million Views</h1>
      </div>
    </div>
    <div className="container">
      <div className="row">
        <div >
          <ul>
          {webtoons.map((webtoon) => (
            <li key={webtoon.id}>
             <Link to={`/webtoons/${webtoon.id}`}>
                      <h2>{webtoon.title}</h2>
                    </Link>
              <img className="col-md-4" src={webtoon.thumbnile} alt={webtoon.title} />
              <p>{webtoon.brief_description}</p>
            </li>
          ))}
        </ul>
          <p>
            <a className="btn btn-secondary" href="#" role="button">
              Add Favourites
            </a>
          </p>
        </div>  
      </div>
      <hr />
    </div>{" "}
    {/* /container */}
  </main>
  <footer className="container">
  </footer>
</>

    </div>
  )
}

export default Homepage