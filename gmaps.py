import googlemaps
from datetime import datetime

class Gmaps:
    APIKEY = "AIzaSyBzOwoGLE6hFrGVw1HAb4RHXhw_HfhGdXw"

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def getDrivingTime(self):
        gmapsClient = googlemaps.Client(key = self.APIKEY)
        direct = gmapsClient.distance_matrix(self.origin, self.destination, mode = "driving", departure_time = "now")
        drivingTime = round(direct['rows'][0]['elements'][0]['duration_in_traffic']['value'] / 60)
        return drivingTime

    def changeOrigin(self, newOrigin):
        self.origin = newOrigin

    def changeDestination(self, newDestination):
        self.destination = newDestination