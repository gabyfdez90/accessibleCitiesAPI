import requests


class OverpassAPI:
    def __init__(self):
        self.overpass_url = "https://overpass-api.de/api/interpreter"

    def query(self, data):
        response = requests.get(self.overpass_url, params={"data": data})
        return response.json()
