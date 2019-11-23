import requests
import base64
import os

subscription_key = "6684ad637c014c709a7568fcb2e2deff"
endpoint = "https://trafficsihthackatum19.cognitiveservices.azure.com/"


def analyze_picture(picture64):
    return_dict = {"trafficLight": False,
                  "green": True,
                  "cars": False}

    analyze_url = endpoint + "vision/v2.1/analyze"

    imgdata = base64.b64decode(picture64)
    filename = 'temp.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    f.close()

    image_path = "/Users/Gamer7000/Desktop/hackatum-2019/temp.jpg"

    image_data = open(image_path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}

    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)

    analysis = response.json()

    os.remove(filename)

    for tag in analysis["description"]["tags"]:
        if tag == "light":
            return_dict["trafficLight"] = True
            if tag == "stoplight":
                return_dict["green"] = False
        if tag == "car" or tag == "bus":
            return_dict["cars"] = True

    return return_dict
