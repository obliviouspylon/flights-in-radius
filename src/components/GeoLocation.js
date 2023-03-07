import React, { } from 'react';

function GeoLocation({lat, lng, inputRadius, setLat, setLng, setMsg, setInputRadius, checkflights}) {

    const getLocation = () => {
        if (!navigator.geolocation) {
            setMsg('Geolocation is not supported by your browser');
        } else {
            setMsg('Locating...');
            navigator.geolocation.getCurrentPosition((position) => {
                setMsg(null);
                setLat(position.coords.latitude);
                setLng(position.coords.longitude);
            }, () => {
                setMsg('Unable to retrieve your location');
            });
        }
    }

    return (
        <div id="GeoLocation">
            <form id="GeoLocation_Form">
                <div className="row mt-3">
                    <div className="form-group">
                        <div className="col-sm">
                            <label htmlFor="GPS_Long">Longitude (E/W)</label>
                        </div>
                        <input type="text" className="form-control" id="GPS_Long" aria-describedby="Longitude" value={lng} onChange={e => setLng(e.target.value)} placeholder="Enter Longitude" />
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="form-group">
                        <div className="col-sm">
                            <label htmlFor="GPS_Lat">Latitude (N/S)</label>
                        </div>
                        <input type="text" className="form-control" id="GPS_Lat" aria-describedby="Latitude" value={lat} onChange={e => setLat(e.target.value)} placeholder="Enter Latitude" />
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="form-group">
                        <div className="col-sm">
                            <label htmlFor="Radius">Radius (km)</label>
                        </div>
                        <input type="text" className="form-control" id="Radius" aria-describedby="Radius" value={inputRadius} onChange={e => setInputRadius(e.target.value)} placeholder="Enter Radius" />
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="col-sm-6">
                        <button type="button" className="btn btn-primary m-2" onClick={getLocation}>Get GPS</button>
                    </div>
                    <div className="col-sm-6">
                        <button type="button" className="btn btn-primary m-2" onClick={checkflights}>Get Planes</button>
                    </div>
                </div>
            </form>
        </div>
    )
}

export default GeoLocation;
