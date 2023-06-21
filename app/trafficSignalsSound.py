import requests


def getTrafficSignalsSoundPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes related with traffic lights 
        that sound when crossing is permitted, because they are very useful in case of visual disabilities.
    """

    # Define queries to Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["crossing"="traffic_signals"]["traffic_signals:sound"="yes"];
    way(area.searchArea)["crossing"="traffic_signals"]["traffic_signals:sound"="yes"];
    relation(area.searchArea)["crossing"="traffic_signals"]["traffic_signals:sound"="yes"];
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
    trafficSignalsSoundCount = int(
        accesibleData["elements"][0]["tags"]["total"])

    # Obtain percentage
    trafficSignalsSoundPercentage = round(
        (trafficSignalsSoundCount / totalCount) * 100, 2)

    return trafficSignalsSoundPercentage
