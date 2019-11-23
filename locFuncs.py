import geocoder
from geopy.geocoders import Nominatim
import requests

azureClientId = "d252ac26-cb9f-4714-9386-d700d9f5f521"
azureSubKey = "JudAesBBTOzxc9vmaZsLo5haaJhMwCX6OFSm5_E-eAk"

locations =

def get_location():
    # Get current location in case we didn't receive one
    # TODO: Rewrite this in JS to use html5 locationing for more accuracy
    return geocoder.ip('me')


# Every 5 location "steps" fetch our direction by getting the difference in latitude and
# difference in longtitude
def get_direction(direction_array):
    directionLat = 0
    directionLong = 0
    for i in range(0, 4):
        directionLat = directionLat + (direction_array[i].latlng[0] - direction_array[i - 1].latlng[0])
        directionLong = directionLong + (direction_array[i].latlng[1] - direction_array[i - 1].latlng[1])
    latlong = [directionLat, directionLong]
    return latlong


def incoming_intersection(latlong):
    geolocator = Nominatim(user_agent="HackaTum2019")
    current = get_location()
    latCurr = current.latlng[0]
    longCurr = current.latlng[1]
    latAfter = current.latlng[0] + latlong[0]
    longAfter = current.latlng[1] + latlong[1]
    curr = get_street(latCurr, longCurr)
    future = get_street(latAfter, longAfter)

    if not curr.street == futre.street:
        return True
    else:
        return False


def get_street(lat, long):
    url = "https://atlas.microsoft.com/search/address/reverse/json?subscription-key=" + str(azureSubKey) + "&api-version=1.0&query=" + str(
        lat) + "," + str(long)
    re = requests.get(url, headers={'x-ms-client-id': azureClientId})
    print(re)
    return re


def