#Set up Webhook using Flash
#https://hackernoon.com/how-to-listen-for-webhooks-using-python-7g153uad
from flask import Flask, request, Response, abort, render_template, send_file
from flask_cors import CORS
import flights_in_radius as FIR

app = Flask(__name__, static_folder="build/static", template_folder="build")
CORS(app)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/flights/index.css")
def indexCSS():
    return send_file('build\static\css\main.38b24421.css')

@app.route("/flights/main.38b24421.css.map")
def indexCSSmap():
    return send_file('build\static\css\main.38b24421.css.map')

@app.route("/flights/arrow.svg")
def arrowSVG():
    return send_file('build/arrow.svg')

@app.route("/flights/manifest.json")
def manifestJSON():
    return send_file('build/manifest.json')

@app.route('/flights/check', methods=['POST'])
def respond():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
      reqJson = request.json
  else:
      print('Content-Type not supported!')
      return ("")
  if (request.method == 'POST') and ('GPS_lon' in reqJson) and ('GPS_lat' in reqJson):
    GPS_lat = float(reqJson['GPS_lat'])
    GPS_lon = float(reqJson['GPS_lon'])
    if "max_radius" in reqJson:
      max_radius = int(reqJson['max_radius'])
      result = FIR.check_flights(GPS_lon,GPS_lat,max_radius)
    else:
      result = FIR.check_flights(GPS_lon,GPS_lat,25)
    return result,200
  else:
    abort(400)

if __name__ == '__main__':
   app.run()
