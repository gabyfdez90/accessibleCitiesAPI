import requests


def getLeisurePercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes which are related with leisure
        (hotels, restaurantes, etc.) which have the tag wheelchair.
    """

    # Define queries to Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
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

    # Send queries for the total and the tagged segment
    accesibleResponse = requests.get(
        overpassUrl, params={"data": accesibleQuery})
    accesibleData = accesibleResponse.json()

    totalResponse = requests.get(overpassUrl, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Process API response
    accesibleFacilities = 0
    if "elements" in accesibleData:
        for element in accesibleData["elements"]:
            if element["type"] == "node":
                accesibleFacilities += 1

    # Obtain percentage
    leisurePercentage = round((accesibleFacilities / totalCount) * 100, 2)

    return leisurePercentage
