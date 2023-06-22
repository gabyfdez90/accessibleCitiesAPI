from app.services.dataCollector import *


def getTactilePavementPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes which are related with tactile paviment
        facilities, which are very useful in case of visual limitations.
    """

    # Define queries to Overpass (Open Street Map)
    dataCollector = DataCollector(city)

    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["highway"="crossing"]["tactile_paving"="yes"];
    way(area.searchArea)["highway"="crossing"]["tactile_paving"="yes"];
    relation(area.searchArea)["highway"="crossing"]["tactile_paving"="yes"];
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

    # Send queries for the total and the tagged segment and process response

    totalCount = dataCollector.getTotalCount2(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount(accesibleQuery)

    # Obtain percentage

    tactilePavementPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return tactilePavementPercentage
