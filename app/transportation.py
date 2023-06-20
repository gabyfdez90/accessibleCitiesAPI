import requests


def getTransportationPercentage(city):
    """
        This function receives the name of a city (str) and returns the percentage of map nodes where 
        public transportation facilities (bus stops, stations, etc) are tagged with wheelchair.
    """

    # Define the queries to Overpass API (Open Street Map)
    overpass_url = "https://overpass-api.de/api/interpreter"
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
    accessibleResponse = requests.get(
        overpass_url, params={"data": accesibleQuery})
    data = accessibleResponse.json()

    totalResponse = requests.get(overpass_url, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Process the data
    accesibleTransportation = 0
    if "elements" in data:
        for element in data["elements"]:
            if element["type"] == "node":
                accesibleTransportation += 1

    # Obtain percentage
    transportationPercentage = round(
        (accesibleTransportation / totalCount) * 100, 2)

    return transportationPercentage
