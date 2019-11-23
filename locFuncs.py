import geocoder
import requests
import json

azureClientId = "d252ac26-cb9f-4714-9386-d700d9f5f521"
azureSubKey = "JudAesBBTOzxc9vmaZsLo5haaJhMwCX6OFSm5_E-eAk"


class LocationHandler():
    def __init__(self):
        self.locations = [None]*5
        self.counter = 0

    def get_location(self):
        # Get current location in case we didn't receive one
        return geocoder.ip('me')

    # Every 5 location "steps" fetch our direction by getting the difference in latitude and
    # difference in longtitude
    def get_direction(self,direction_array):
        directionLat = 0
        directionLong = 0
        for i in range(0, 3):
            directionLat = directionLat + (direction_array[i].latlng[0] - direction_array[i - 1].latlng[0])
            directionLong = directionLong + (direction_array[i].latlng[1] - direction_array[i - 1].latlng[1])
        direction = [directionLat, directionLong]
        return direction

    def incoming_intersection(self,direction_array):
        direction = self.get_direction(direction_array)
        current = self.get_location()
        latCurr = current.latlng[0]
        longCurr = current.latlng[1]
        latAfter = current.latlng[0] + direction[0]
        longAfter = current.latlng[1] + direction[1]

        curr = self.get_street(latCurr, longCurr)
        future = self.get_street(latAfter, longAfter)

        # If they're still the same, user can continue walking down the street without hitting another one
        # If they're different, user will soon hit a different street and walk into an intersection, return true
        if curr == future:
            return False
        else:
            return True

    def get_street(self,lat, long):
        url = "https://atlas.microsoft.com/search/address/reverse/json?subscription-key=" + str(
            azureSubKey) + "&api-version=1.0&query=" + str(lat) + "," + str(long)
        re = requests.get(url, headers={'x-ms-client-id': azureClientId})
        re_json = json.loads(re.text)
        return re_json["addresses"][0]["address"]["street"]

    def do_locationing(self,location=None):
        if location is None:
            location = self.get_location()

        self.locations[self.counter] = location

        if self.counter == 4:
            intersection = self.incoming_intersection(self.locations)
            self.counter = 0
            return intersection

        else:
            self.counter = self.counter + 1
            return False
