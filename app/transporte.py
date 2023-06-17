import requests


def obtenerTransporte(ciudad):
    """
        Esta función recibe el nombre de la ciudad (str) y devuelve el porcentaje de nodos del mapa que están relacionados
        con transporte público (estaciones, paradas, vehículos, etc.) y que tienen el tag "wheelchair".
    """

    # Definir las consultas necesarias a la API de Overpass (Open Street Map)
    overpass_url = "https://overpass-api.de/api/interpreter"
    accesibleQuery = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
    node(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"]["wheelchair"="yes"];
    way(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"]["wheelchair"="yes"];
    relation(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"]["wheelchair"="yes"];
    );
    out;

    """

    totalQuery = f"""
    [out:json];
    area[name="{ciudad}"]->.searchArea;
    (
    node(area.searchArea)["public_transport"~"^(stop_position|station|vehicle)$"];
    );
    out count;
    """

    # Enviar las consultas de elementos totales y accesibles a la API
    accessibleResponse = requests.get(
        overpass_url, params={"data": accesibleQuery})
    data = accessibleResponse.json()

    totalResponse = requests.get(overpass_url, params={"data": totalQuery})
    totalData = totalResponse.json()
    totalCount = int(totalData["elements"][0]["tags"]["total"])

    # Procesar los datos
    accesibleTransportation = 0
    if "elements" in data:
        for element in data["elements"]:
            if element["type"] == "node":
                accesibleTransportation += 1

    # Obtener porcentaje
    porcentajeTransporte = round(
        (accesibleTransportation / totalCount) * 100, 2)

    return porcentajeTransporte
