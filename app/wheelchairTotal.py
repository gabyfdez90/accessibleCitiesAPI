import requests


def getWheelchairPercentage(city):
    """
    This function receives the name of a city (str) and returns the percentage of nodes that includes the tag wheelchair.
    """


# Define the queries to Overpass API (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
      node["wheelchair"="yes"](area.searchArea);
      way["wheelchair"="yes"](area.searchArea);
      relation["wheelchair"="yes"](area.searchArea);
    );
    out;
    """

    queryTotal = f"""
    [out:json];
    area[name="{city}"]->.searchArea;
    (
      node["wheelchair"~"^(yes|no)$"](area.searchArea);
      way["wheelchair"~"^(yes|no)$"](area.searchArea);
      relation["wheelchair"~"^(yes|no)$"](area.searchArea);
    );
    out;
    """

    # Send the querys to OverPass
    response = requests.get(overpassUrl, params={"data": query})
    data = response.json()

    responseTotal = requests.get(overpassUrl, params={"data": queryTotal})
    dataTotal = responseTotal.json()

    # Obtein the total amount of elements
    totalNodes = len(dataTotal["elements"])
    wheelchairNodes = 0

    for element in data["elements"]:
        tags = element.get("tags", {})
        if "wheelchair" in tags and tags["wheelchair"] == "yes":
            wheelchairNodes += 1

    # Obtener porcentaje
    wheelchairPercentage = int((wheelchairNodes / totalNodes) * 100)

    # Imprimir los resultados
    # print("Número total de nodos:", totalNodos)
    # print("Nodos con wheelchair=yes:", nodosWheelchair)
    # print("Porcentaje de nodos con wheelchair=yes sobre el total:",
    #       porcentajeWheelchair, "%")

    return wheelchairPercentage
