import requests


def obtenerOcio(ciudad):
    """
        Esta función recibe el nombre de la ciudad (str) y devuelve el porcentaje de nodos del mapa que están relacionados
        con ocio (hoteles, restaurantes, etc.) y que tienen el tag "wheelchair".
    """

    # Definir las consultas necesarias a la API de Overpass (Open Street Map)
    overpassUrl = "https://overpass-api.de/api/interpreter"
    accesibleQuery = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
    node(area.searchArea)["amenity"~"^(restaurant|hotel|shop)$"]["wheelchair"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
    node(area.searchArea)["amenity"~"^(restaurant|hotel|shop)$"];
    );
    out count;
    """

    # Enviar las consultas de elementos totales y accesibles a la API
    accesibleResponse = requests.get(
        overpassUrl, params={"data": accesibleQuery})
    accesibleData = accesibleResponse.json()

    totalResponse = requests.get(overpassUrl, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Procesar la respuesta de la API
    accesibleFacilities = 0
    if "elements" in accesibleData:
        for element in accesibleData["elements"]:
            if element["type"] == "node":
                accesibleFacilities += 1

    # Obtener porcentaje
    porcentajeOcio = round((accesibleFacilities / totalCount) * 100, 2)

    return porcentajeOcio
