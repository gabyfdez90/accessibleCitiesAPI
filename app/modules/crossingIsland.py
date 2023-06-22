from app.services.dataCollector import *


def getCrossingIslandPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes which are related with tactile paviment
        facilities, which are very useful in case of visual limitations.
    """

    # Define queries to Overpass (Open Street Map)

    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["highway"="crossing"]["crossing_island"="yes"];
    way(area.searchArea)["highway"="crossing"]["crossing_island"="yes"];
    relation(area.searchArea)["highway"="crossing"]["crossing_island"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["highway"="crossing"];
    way(area.searchArea)["highway"="crossing"];
    relation(area.searchArea)["highway"="crossing"];
    );
    out count;
    """

    dataCollector = DataCollector(city)

    # Send queries and process response data

    totalCount = dataCollector.getTotalCount(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount(accesibleQuery)

    # Obtain percentage
    crossingIslandPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return crossingIslandPercentage
