import requests


def obtenerParking(ciudad):
    """
        Esta función recibe el nombre de la ciudad (str) y devuelve el porcentaje de nodos del mapa que están relacionados
        con parking (accesibilidad en plazas, etc.) y que tienen el tag "wheelchair".
    """

    # Definir las consultas necesarias a la API de Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    accessibleQuery = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
    node(area.searchArea)["amenity"="parking"]["access"~"^(yes|permissive|designated)$"]["wheelchair"="yes"];
    way(area.searchArea)["amenity"="parking"]["access"~"^(yes|permissive|designated)$"]["wheelchair"="yes"];
    relation(area.searchArea)["amenity"="parking"]["access"~"^(yes|permissive|designated)$"]["wheelchair"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
    node(area.searchArea)["amenity"="parking"];
    way(area.searchArea)["amenity"="parking"];
    relation(area.searchArea)["amenity"="parking"];
    );
    out count;
    """

    # Enviar las consultas de elementos totales y accesibles a la API
    accessibleResponse = requests.get(
        overpassUrl, params={"data": accessibleQuery})
    accesibleData = accessibleResponse.json()

    totalResponse = requests.get(overpassUrl, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Procesar la respuesta para elementos accesibles
    accessibleParking = 0
    if "elements" in accesibleData:
        for element in accesibleData["elements"]:
            if element["type"] == "node" or element["type"] == "way":
                accessibleParking += 1

     # Obtener porcentaje
    porcentajeParking = round((accessibleParking / totalCount) * 100, 2)

    return porcentajeParking
