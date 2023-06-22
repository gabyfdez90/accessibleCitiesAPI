from app.services.dataCollector import *


def getTrafficSignalsSoundPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes related with traffic lights 
        that sound when crossing is permitted, because they are very useful in case of visual disabilities.
    """

    # Define queries to Overpass (Open Street Map)
    dataCollector = DataCollector(city)

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

    # Send queries and process responses

    totalCount = dataCollector.getTotalCount2(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount2(accesibleQuery)

    # Obtain percentage

    trafficSignalsSoundPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return trafficSignalsSoundPercentage
