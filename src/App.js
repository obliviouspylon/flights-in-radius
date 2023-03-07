import React, { useEffect, useState } from 'react';

import './App.css';
import Radar from './components/radar';
import GeoLocation from './components/GeoLocation';

function App() {

  // let planeInfo = [[0.2, -0.3, 260],[-0.2, -0.6, 105]]
  const [planeInfo, setPlaneInfo] = useState([[]]);
  const [inputRadius, setInputRadius] = useState(20);
  const [max_radius, setMax_radius] = useState(20);

  const [lat, setLat] = useState(43.686540); //Default to PEarson airport
  const [lng, setLng] = useState(-79.612208); //Default to PEarson airport

  const [msg, setMsg] = useState("");

  const checkflights = () => {
    fetch(`/flights/check`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'GPS_lat': lat,
        'GPS_lon': lng,
        'max_radius': inputRadius
      })
    })
      .then(response => response.json())
      .then(data => {
        setMsg(data.message.split('\n').map(i => {
          return <p>{i}</p>
        }))
        setPlaneInfo(data.planes)
        setMax_radius(data.max_radius)
      });
  }

  useEffect(() => {
    // setPlaneInfo([[0.5, 0.5, 170, "1"],
    //   [-0.5, 0.1, 50, "2"],
    //   [0.5, 0, 10, "3"]])
  }, []);

  return (
    <div className="App">
      <header className="App-header">
      </header>
      <GeoLocation lat={lat} lng={lng} inputRadius={inputRadius} setLat={setLat} setLng={setLng} setMsg={setMsg} setInputRadius={setInputRadius} checkflights={checkflights} />
      {msg}
      <Radar planeInfo={planeInfo} max_radius={max_radius} /><br />
    </div>
  );
}

export default App;
