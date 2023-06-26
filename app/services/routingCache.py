import redis
import json
from app.modules.wheelchairTotal import *
from app.modules.leisure import *
from app.modules.transportation import *
from app.modules.parking import *
from app.modules.pavement import *
from app.modules.trafficSignalsSound import *
from app.modules.trafficSignalsVibration import *
from app.modules.crossingIsland import *

cache = redis.Redis(host='localhost', port=6379, db=0)


def checkCacheForData(city):
    """
    This function checks if the data of a given city is already available in the local
    Redis cache, if is not, it calls the function that is responsible for fetching 
    Overpass data and stores its content for faster requests.
    """
    data = cache.get(city)
    if data is not None:
        return data.decode('utf-8')
    else:
        data = fetchDataFromOverpassAPI(city)
        if data:
            cache.set(city, data)
            return data
        else:
            return None


def fetchDataFromOverpassAPI(city):
    """
    This function returns a json with the data of a given city obtained from Overpass API,
    because it wasn't in Redis cache.
    """

    cityPercentage = getWheelchairPercentage(city)
    leisurePercentage = getLeisurePercentage(city)
    transportationPercentage = getTransportationPercentage(city)
    parkingPercentage = getParkingPercentage(city)
    tactilePavementPercentage = getTactilePavementPercentage(city)
    trafficSignalsSound = getTrafficSignalsSoundPercentage(city)
    trafficSignalsVibration = getTrafficSignalsVibrationPercentage(city)

    cityData = {
        "wheelchairAccessibility": cityPercentage,
        "wheelchairFacilitiesInLeisure": leisurePercentage,
        "wheelchairTransportation": transportationPercentage,
        "wheelchairParking": parkingPercentage,
        "tactilePavement": tactilePavementPercentage,
        "trafficSignalsSound": trafficSignalsSound,
        "trafficSignalsVibration": trafficSignalsVibration,
    }

    jsonData = json.dumps(cityData)

    return jsonData
