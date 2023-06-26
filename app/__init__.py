from flask import Flask, jsonify
from http import HTTPStatus
import json
from app.services.routingCache import checkCacheForData

app = Flask(__name__)


@app.route("/api/<string:city1>/<string:city2>")
def compareCities(city1, city2):

    city1Format = city1.capitalize()
    city2Format = city2.capitalize()

    city1Data = json.loads(checkCacheForData(city1Format))
    city2Data = json.loads(checkCacheForData(city2Format))

    cityPercentage1 = city1Data['wheelchairAccessibility']
    cityPercentage2 = city2Data['wheelchairAccessibility']

    leisurePercentage1 = city1Data["wheelchairFacilitiesInLeisure"]
    leisurePercentage2 = city2Data["wheelchairFacilitiesInLeisure"]

    transportationPercentage1 = city1Data["wheelchairTransportation"]
    transportationPercentage2 = city2Data["wheelchairTransportation"]

    parkingPercentage1 = city1Data["wheelchairTransportation"]
    parkingPercentage2 = city2Data["wheelchairTransportation"]

    tactilePavementPercentage1 = city1Data["tactilePavement"]
    tactilePavementPercentage2 = city2Data["tactilePavement"]

    trafficSignalsSound1 = city1Data["trafficSignalsSound"]
    trafficSignalsSound2 = city2Data["trafficSignalsSound"]

    trafficSignalsVibration1 = city1Data["trafficSignalsVibration"]
    trafficSignalsVibration2 = city2Data["trafficSignalsVibration"]

    if cityPercentage1 == 0.0:
        return jsonify({
            "status": "OK",
            "message": f"Sorry, {city1Format} isn't in Open Street Map."
        })
    if cityPercentage2 == 0.0:
        return jsonify({
            "status": "OK",
            "message": f"Sorry, {city2Format} isn't in Open Street Map."
        })

    else:
        return jsonify(
            {
                "status": "OK",
                "message": "Succesful request",

                "city1": {
                    "name": city1Format,
                    "wheelchairAccessibility": cityPercentage1,
                    "wheelchairFacilitiesInLeisure": leisurePercentage1,
                    "wheelchairTransportation": transportationPercentage1,
                    "wheelchairParking": parkingPercentage1,
                    "tactilePavement": tactilePavementPercentage1,
                    "trafficSignalsSound": trafficSignalsSound1,
                    "trafficSignalsVibration": trafficSignalsVibration1
                },

                "city2": {
                    "name": city2Format,
                    "wheelchairAccessibility": cityPercentage2,
                    "wheelchairFacilitiesInLeisure": leisurePercentage2,
                    "wheelchairTransportation": transportationPercentage2,
                    "wheelchairParking": parkingPercentage2,
                    "tactilePavement": tactilePavementPercentage2,
                    "trafficSignalsSound": trafficSignalsSound2,
                    "trafficSignalsVibration": trafficSignalsVibration2
                }
            }
        ), HTTPStatus.OK
