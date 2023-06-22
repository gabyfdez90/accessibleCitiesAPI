from app.services.dataCollector import *


def getWheelchairPercentage(city):
    """
    This function receives the name of a city (str) and returns the percentage of nodes that includes the tag wheelchair.
    """


# Define the queries to Overpass API (Open Street Map)

    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
      node(area.searchArea)["wheelchair"="yes"];
      way(area.searchArea)["wheelchair"="yes"];
      relation(area.searchArea)["wheelchair"="yes"];
    );
    out;
    """

    queryTotal = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
      node(area.searchArea)["wheelchair"~"^(yes|no)$"];
      way(area.searchArea)["wheelchair"~"^(yes|no)$"];
      relation(area.searchArea)["wheelchair"~"^(yes|no)$"];
    );
    out;
    """

    # Send the querys to OverPass

    dataCollector = DataCollector(city)

    # Obtein the total amount of elements

    totalCount = dataCollector.getTotalCount(queryTotal)
    accessibleCount = dataCollector.getAccessibleCount(accesibleQuery)

    # Obtein percentage
    wheelchairPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return wheelchairPercentage
