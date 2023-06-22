from flask import Flask, jsonify
from http import HTTPStatus
from app.modules.wheelchairTotal import *
from app.modules.leisure import *
from app.modules.transportation import *
from app.modules.parking import *
from app.modules.pavement import *
from app.modules.trafficSignalsSound import *
from app.modules.trafficSignalsVibration import *
from app.modules.crossingIsland import *

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

    tactilePavementPercentage1 = getTactilePavementPercentage(city1Format)
    tactilePavementPercentage2 = getTactilePavementPercentage(city2Format)

    trafficSignalsSound1 = getTrafficSignalsSoundPercentage(city1Format)
    trafficSignalsSound2 = getTrafficSignalsSoundPercentage(city2Format)

    trafficSignalsVibration1 = getTrafficSignalsVibrationPercentage(
        city1Format)
    trafficSignalsVibration2 = getTrafficSignalsVibrationPercentage(
        city2Format)

    crossingIslands1 = getCrossingIslandPercentage(city1Format)
    crossingIslands2 = getCrossingIslandPercentage(city2Format)

    return jsonify(
        {
            "status": "OK",

            "city1": {
                "name": city1Format,
                "wheelchairAccessibility": cityPercentage1,
                "wheelchairFacilitiesInLeisure": leisurePercentage1,
                "wheelchairTransportation": transportationPercentage1,
                "wheelchairParking": parkingPercentage1,
                "tactilePavement": tactilePavementPercentage1,
                "trafficSignalsSound": trafficSignalsSound1,
                "trafficSignalsVibration": trafficSignalsVibration1,
                "crossingIslands": crossingIslands1
            },

            "city2": {
                "name": city2Format,
                "wheelchairAccessibility": cityPercentage2,
                "wheelchairFacilitiesInLeisure": leisurePercentage2,
                "wheelchairTransportation": transportationPercentage2,
                "wheelchairParking": parkingPercentage2,
                "tactilePavement": tactilePavementPercentage2,
                "trafficSignalsSound": trafficSignalsSound2,
                "trafficSignalsVibration": trafficSignalsVibration2,
                "crossingIslands": crossingIslands2
            }
        }
    ), HTTPStatus.OK
