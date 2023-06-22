from app.services.dataCollector import *


def getLeisurePercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes which are related with leisure
        (hotels, restaurantes, etc.) which have the tag wheelchair.
    """

    dataCollector = DataCollector(city)

    # Define queries to Overpass (Open Street Map)

    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["amenity"~"^(restaurant|hotel|shop)$"]["wheelchair"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["amenity"~"^(restaurant|hotel|shop)$"];
    );
    out count;
    """

    # Send queries and process response

    totalCount = dataCollector.getTotalCount2(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount(accesibleQuery)

    # Obtain percentage

    leisurePercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return leisurePercentage
