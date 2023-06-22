from app.services.dataCollector import *


def getTrafficSignalsVibrationPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes related with traffic lights 
        with a vibration device to be used by persons with visual disabilities.
    """

    dataCollector = DataCollector(city)

    # Define queries to Overpass (Open Street Map)

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

    # Send queries and process data

    totalCount = dataCollector.getTotalCount2(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount2(accesibleQuery)

    # Process API response

    trafficSignalsVibrationPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return trafficSignalsVibrationPercentage
