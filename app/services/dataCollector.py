from app.services.overpassConnection import *


class DataCollector:
    """
    This class provides a set of methods to obtain data values
    from Overpass querys and process them as total count, accessible
    count and percentage. 
    """

    def __init__(self, city):
        self.city = city
        self.overpass_api = OverpassAPI()

    def getTotalCount(self, query):
        data = self.overpass_api.query(query)
        return len(data["elements"])

    def getTotalCount2(self, query):
        data = self.overpass_api.query(query)
        if "elements" in data:
            return int(data["elements"][0]["tags"]["total"])
        return 0

    def getAccessibleCount(self, query):
        data = self.overpass_api.query(query)
        return len(data.get("elements", []))

    def getAccessibleCount2(self, query):
        data = self.overpass_api.query(query)
        return int(data["elements"][0]["tags"]["total"])

    def getPercentage(self, accessible_count, total_count):
        if total_count > 0:
            return round((accessible_count / total_count) * 100, 2)
        return 0.0
