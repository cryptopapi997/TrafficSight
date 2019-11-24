import requests
import base64
import os
from PIL import Image
import io

subscription_key = "[YOUR KEY]"
endpoint = "https://trafficsihthackatum19.cognitiveservices.azure.com/"

def crop_out_image(filename, x,w,y,h):
    im = Image.open(r"[YOUR_PATH]" + filename)

    crop = im.crop((x, y, x+w, y+h))

    file_name = "temp2"
    image_path = "[YOUR PATH]" + file_name

    crop.save(image_path,'JPEG')

    image_data = open(image_path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}

    params = {'visualFeatures': 'Description, Tags, Categories'}
    analyze_url = endpoint + "vision/v2.1/analyze"

    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)

    analysis = response.json()

    for tag in analysis["tags"]:
        if tag["name"] == "green":
            os.remove("temp2.jpeg")
            return True
    os.remove("temp2.jpeg")
    return False

def blob_to_image_converter(profile_image_blob):

   if profile_image_blob is not None and len(profile_image_blob) > 0:
       image = base64.b64decode(str(profile_image_blob))

       file_name = "temp"
       fileExtension = '.jpeg'
       file_name += fileExtension

       image_path = "[YOUR PATH]" + file_name

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

    params = {'visualFeatures': 'Objects'}

    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)

    analysis = response.json()


    for object in analysis["objects"]:
        if object["object"] == "traffic light":
            return_dict["green"] = crop_out_image(filename,[object][0]["rectangle"]["x"],
                                                  [object][0]["rectangle"]["w"],[object][0]["rectangle"]["y"],
                                                  [object][0]["rectangle"]["h"])
            return_dict["trafficLight"] = True
            if object == "stoplight":
                return_dict["green"] = False
        if object == "car" or object == "bus":
            return_dict["cars"] = True

    os.remove(filename)
    return return_dict
