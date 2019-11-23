import requests
import base64
import os
from PIL import Image
import io
import uuid

subscription_key = "6684ad637c014c709a7568fcb2e2deff"
endpoint = "https://trafficsihthackatum19.cognitiveservices.azure.com/"

def blob_to_image_converter(profile_image_blob):

   if profile_image_blob is not None and len(profile_image_blob) > 0:
       image = base64.b64decode(str(profile_image_blob))

       #set fileName
       file_name = "temp"
       fileExtension = '.jpeg'
       file_name += fileExtension

       image_path = "/Users/Gamer7000/Desktop/hackatum-2019/" + file_name

       im = Image.open(io.BytesIO(image))
       im.save(image_path, 'jpeg')
       path = image_path
       return path, file_name

def analyze_picture(picture64):
    return_dict = {"trafficLight": False,
                  "green": True,
                  "cars": False}

    analyze_url = endpoint + "vision/v2.1/analyze"

    filename = "temp.jpeg"

    image_path,filename = blob_to_image_converter(picture64)

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
