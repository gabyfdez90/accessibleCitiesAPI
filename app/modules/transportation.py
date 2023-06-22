from app.services.dataCollector import *


def getTransportationPercentage(city):
    """
        This function receives the name of a city (str) and returns the percentage of map nodes where 
        public transportation facilities (bus stops, stations, etc) are tagged with wheelchair.
    """

    dataCollector = DataCollector(city)

    # Define the queries to Overpass API (Open Street Map)

    accesibleQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"]["wheelchair"="yes"];
    way(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"]["wheelchair"="yes"];
    relation(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"]["wheelchair"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
    node(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"];
    );
    out count;
    """

    # Send the queries to obtain the total and accesible segment of nodes

    totalCount = dataCollector.getTotalCount2(totalQuery)
    accessibleCount = dataCollector.getAccessibleCount(accesibleQuery)

    # Obtain percentage

    transportationPercentage = dataCollector.getPercentage(
        accessibleCount, totalCount)

    return transportationPercentage
