from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import requests

from PIL import Image
from array import array
import os
import sys
import time
import tempfile
import io
subscription_key = "6684ad637c014c709a7568fcb2e2deff"
endpoint = "https://trafficsihthackatum19.cognitiveservices.azure.com/"


def analyze_picture():
    print("he")
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # INPUT HERE
    remote_image_url = "https://cml.sad.ukrd.com/image/640100-3600x2700.jpg"

    # Call API with URL
    detect_objects_results_remote = computervision_client.detect_objects(remote_image_url)

    # RESULTS
    x, w, y, h = 0, 0, 0, 0

    if len(detect_objects_results_remote.objects) == 0:
        print("No objects detected.")
    else:
        for object in detect_objects_results_remote.objects:
            if object.object_property == "traffic light":
                x = object.rectangle.x
                w = object.rectangle.x + object.rectangle.w
                y = object.rectangle.y
                h = object.rectangle.y + object.rectangle.h
                print("yuh")

analyze_url = endpoint + "vision/v2.1/analyze"

# Set image_path to the local path of an image that you want to analyze.
image_path = "C:/Documents/ImageToAnalyze.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)

