import requests


def getTrafficSignalsVibrationPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes related with traffic lights 
        with a vibration device to be used by persons with visual disabilities.
    """

    # Define queries to Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["crossing"="traffic_signals"]["traffic_signals:vibration"="yes"];
    way(area.searchArea)["crossing"="traffic_signals"]["traffic_signals:vibration"="yes"];
    relation(area.searchArea)["crossing"="traffic_signals"]["traffic_signals:vibration"="yes"];
    );
    out count;
    """

    totalQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["crossing"="traffic_signals"];
    way(area.searchArea)["crossing"="traffic_signals"];
    relation(area.searchArea)["crossing"="traffic_signals"];
    );
    out count;
    """

    # Send queries for the total and the tagged segment
    accesibleResponse = requests.get(
        overpassUrl, params={"data": accesibleQuery})
    accesibleData = accesibleResponse.json()

    totalResponse = requests.get(overpassUrl, params={"data": totalQuery})
    totalData = totalResponse.json()

    # Process API response
    totalCount = int(totalData["elements"][0]["tags"]["total"])
    trafficSignalsVibrationCount = int(
        accesibleData["elements"][0]["tags"]["total"])

    # Obtain percentage
    trafficSignalsVibrationPercentage = round(
        (trafficSignalsVibrationCount / totalCount) * 100, 2)

    return trafficSignalsVibrationPercentage
