import requests


def getParkingPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of map nodes which are
        related with parking and have the tag wheelchair on them.
    """

    # Define queries to Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    accessibleQuery = f"""
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

    # Send queries and get response
    accessibleResponse = requests.get(
        overpassUrl, params={"data": accessibleQuery})
    accesibleData = accessibleResponse.json()

    totalResponse = requests.get(overpassUrl, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Process response
    accessibleParking = 0
    if "elements" in accesibleData:
        for element in accesibleData["elements"]:
            if element["type"] == "node" or element["type"] == "way":
                accessibleParking += 1

     # Obtain percentage
    parkingPercentage = round((accessibleParking / totalCount) * 100, 2)

    return parkingPercentage
