import "./App.css";
import {useState,useEffect} from 'react';
import axios from "axios";
function App() {
  
   

  
  const [recommendations, setRecommendations] = useState([]);


   useEffect(() => {
     axios.get('http://localhost:5000/api')
     .then(response=>{setRecommendations(response.data)})
     .catch(error=>{ console.log(error)})
   }, [])
   
  



return (
  <div>
      <>
<form className="d-flex mt-5" role="search">
      <input className="form-control me-2" id="ip" type="search" name="search" placeholder="Search" aria-label="Search" />
      <button className="btn btn-success"   type="submit">Search</button>
</form>
  
 <div className="apprec">
  <div className="App">
    <div className="head">
      <div>
        <h1>Music Recommender</h1>
        <p>Get proper recommendations and enjoy listening!</p>
      </div>
    </div>
    
  </div>

  <div className="rec">
    <div className="show">
      <h2>Recommended Music for you:</h2>
      <table className="table table-hover table-light">
      <thead>
        <tr>
          <th>Song</th>
          <th>Artist</th>
        </tr>
      </thead>
      <tbody>
      {recommendations.slice(0,10).map(recommendation => (
        <tr key={recommendation.id}>
          <td>{recommendation.song}</td>
          <td>{recommendation.artist}</td>
        </tr>
      ))}
      </tbody>
    </table>
    </div>
  </div>
 </div>
 </> 
  </div>
)
}

export default App;