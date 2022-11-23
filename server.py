#Set up Webhook using Flash
#https://hackernoon.com/how-to-listen-for-webhooks-using-python-7g153uad
from flask import Flask, request, Response, abort
from flask_cors import CORS
import flights_in_radius as FIR

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def respond():
  if (request.method == 'GET') and (None != request.args.get('GPS_lat')) and (None != request.args.get('GPS_lat')):
    GPS_lat = float(request.args.get('GPS_lat'))
    GPS_lon = float(request.args.get('GPS_lon'))
    return FIR.main(GPS_lat,GPS_lon),200
  else:
    abort(400)

if __name__ == '__main__':
   app.run()
