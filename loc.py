import requests
from flask import Flask, request
import locFuncs

app = Flask(__name__)

@app.route('/get-traffic-info')
def getTrafficInfo():
    location = request.args.get('location')
    if not location is None:





# Obs ne ampel gibt und welche farbe
#Auto
# Kreuzung




direction_array = [None]*(5)

for i in range(0,5):
    direction_array[i] = get_location()

latlong = get_direction(direction_array)
incoming_intersection(latlong)

