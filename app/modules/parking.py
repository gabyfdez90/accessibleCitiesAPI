from app.services.dataCollector import *


def getParkingPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of map nodes which are
        related with parking and have the tag wheelchair on them.
    """

    dataCollector = DataCollector(city)

    # Define queries to Overpass (Open Street Map)

    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["amenity"="parking"]["access"~"^(yes|permissive|designated)$"]["wheelchair"="yes"];
    way(area.searchArea)["amenity"="parking"]["access"~"^(yes|permissive|designated)$"]["wheelchair"="yes"];
    relation(area.searchArea)["amenity"="parking"]["access"~"^(yes|permissive|designated)$"]["wheelchair"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["amenity"="parking"];
    way(area.searchArea)["amenity"="parking"];
    relation(area.searchArea)["amenity"="parking"];
    );
    out count;
    """

    # Send queries and process response

    totalCount = dataCollector.getTotalCount2(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount(accesibleQuery)

    # Obtain percentage

    parkingPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return parkingPercentage
