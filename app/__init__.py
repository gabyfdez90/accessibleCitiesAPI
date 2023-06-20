from flask import Flask, jsonify
from http import HTTPStatus
from app.wheelchairTotal import *
from app.leisure import *
from app.transportation import *
from app.parking import *

app = Flask(__name__)


@app.route("/api/<string:city1>/<string:city2>")
def compareCities(city1, city2):

    city1Format = city1.capitalize()
    city2Format = city2.capitalize()

    cityPercentage1 = getWheelchairPercentage(city1Format)
    cityPercentage2 = getWheelchairPercentage(city2Format)

    leisurePercentage1 = getLeisurePercentage(city1Format)
    leisurePercentage2 = getLeisurePercentage(city2Format)

    transportationPercentage1 = getTransportationPercentage(city1Format)
    transportationPercentage2 = getTransportationPercentage(city2Format)

    parkingPercentage1 = getParkingPercentage(city1Format)
    parkingPercentage2 = getParkingPercentage(city2Format)

    return jsonify(
        {
            "status": "OK",

            "city1": {
                "name": city1Format,
                "wheelchairAccessibility": cityPercentage1,
                "wheelchairFacilitiesInLeisure": leisurePercentage1,
                "wheelchairTransportation": transportationPercentage1,
                "wheelchairParking": parkingPercentage1
            },

            "city2": {
                "name": city2Format,
                "wheelchairAccessibility": cityPercentage2,
                "wheelchairFacilitiesInLeisure": leisurePercentage2,
                "wheelchairTransportation": transportationPercentage2,
                "wheelchairParking": parkingPercentage2
            }
        }
    ), HTTPStatus.OK
