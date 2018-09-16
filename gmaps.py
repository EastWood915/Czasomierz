import googlemaps
from datetime import datetime

def getDrivingTime(startPoint, destPoint):
    """Get travel time between two points using Google Maps """
    gmaps = googlemaps.Client(key = "AIzaSyBzOwoGLE6hFrGVw1HAb4RHXhw_HfhGdXw")

    direct = gmaps.distance_matrix("Bochenka 25", "50.0441996, 19.9664313", mode = "driving", departure_time = "now")
    drivingTime = round(direct['rows'][0]['elements'][0]['duration_in_traffic']['value'] / 60)

    return(drivingTime)