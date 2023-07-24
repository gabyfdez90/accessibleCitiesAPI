import requests


class OverpassAPI:
    """
    This class connects to Overpass API through its free endpoint, query
    the data and returns a json.
    """

    def __init__(self):
        self.overpass_url = "https://overpass-api.de/api/interpreter"

    def query(self, data):
        response = requests.get(self.overpass_url, params={"data": data})
        return response.json()
