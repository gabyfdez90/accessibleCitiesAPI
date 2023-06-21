import requests


def getTactilePavementPercentage(city):
    """
        This function receives the name of the city (str) and returns the percentage of nodes which are related with tactile paviment
        facilities, which are very useful in case of visual limitations.
    """

    # Define queries to Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
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

    # Send queries for the total and the tagged segment
    accesibleResponse = requests.get(
        overpassUrl, params={"data": accesibleQuery})
    accesibleData = accesibleResponse.json()

    totalResponse = requests.get(overpassUrl, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Process API response
    accesiblePavement = 0
    if "elements" in accesibleData:
        for element in accesibleData["elements"]:
            if element["type"] == "node":
                accesiblePavement += 1

    # Obtain percentage
    tactilePavementPercentage = round(
        (accesiblePavement / totalCount) * 100, 2)

    return tactilePavementPercentage
