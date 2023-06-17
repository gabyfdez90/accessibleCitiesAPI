import requests


def obtenerPorcentajeCiudad(ciudad):
    """
    Esta función recibe el nombre de la ciudad (str) y devuelve el porcentaje de nodos del mapa que tiene el tag "wheelchair"
    o silla de ruedas.
    """


# Definir las consultas necesarias a la API de Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
      node["wheelchair"="yes"](area.searchArea);
      way["wheelchair"="yes"](area.searchArea);
      relation["wheelchair"="yes"](area.searchArea);
    );
    out;
    """

    queryTotal = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
      node["wheelchair"~"^(yes|no)$"](area.searchArea);
      way["wheelchair"~"^(yes|no)$"](area.searchArea);
      relation["wheelchair"~"^(yes|no)$"](area.searchArea);
    );
    out;
    """

    # Enviar las consultas a OverPass
    response = requests.get(overpassUrl, params={"data": query})
    data = response.json()

    responseTotal = requests.get(overpassUrl, params={"data": queryTotal})
    dataTotal = responseTotal.json()

    # Obtener el total de elementos o nodos del mapa de la ciudad
    totalNodos = len(dataTotal["elements"])
    nodosWheelchair = 0

    for element in data["elements"]:
        tags = element.get("tags", {})
        if "wheelchair" in tags and tags["wheelchair"] == "yes":
            nodosWheelchair += 1

    # Obtener porcentaje
    porcentajeWheelchair = int((nodosWheelchair / totalNodos) * 100)

    # Imprimir los resultados
    # print("Número total de nodos:", totalNodos)
    # print("Nodos con wheelchair=yes:", nodosWheelchair)
    # print("Porcentaje de nodos con wheelchair=yes sobre el total:",
    #       porcentajeWheelchair, "%")

    return porcentajeWheelchair
