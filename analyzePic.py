import requests

subscription_key = "6684ad637c014c709a7568fcb2e2deff"
endpoint = "https://trafficsihthackatum19.cognitiveservices.azure.com/"


def analyze_picture():
    #TODO: Convert pic to jpg

    return_dict = {"trafficLight": False,
                  "canCross": False,
                  "cars": False}

    analyze_url = endpoint + "vision/v2.1/analyze"

    image_path = "/Users/Gamer7000/Desktop/Stop_Light_Wide.jpg"

    image_data = open(image_path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}

    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)

    analysis = response.json()

    for tag in analysis["description"]["tags"]:
        if tag == "light":
            return_dict["trafficLight"] = True
            if tag == "green":
                return_dict["canCross"] = True
        if tag == "car" or tag == "bus":
            return_dict["cars"] = True


analyze_picture()

