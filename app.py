from flask import Flask, render_template, request
import os
import requests
import json
import time
import replicate

# os.environ["REPLICATE_API_TOKEN"] = "r8_8KikJnNAhhr7wVJtLBa0w0L7QvaACoM3ktx1J"

# Set up the API endpoint and headers
url = "https://api.replicate.ai/v1/models/laion-ai/ongo/predict"
headers = {
    "Authorization": "r8_8KikJnNAhhr7wVJtLBa0w0L7QvaACoM3ktx1J",
    "Content-Type": "application/json",
}

# Set up the input data
data = {
    "prompt": "a beautiful painting of a sunset over the ocean",
    "guidance_scale": 10.0,
    "total_steps": 250,
    "init_skip_fraction": 0.35,
    "batch_size": 3,
}

# Send the request to the API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Get the image URL from the response
image_url = response.json()["outputs"][0]["data"]["image_url"]

# Download the image
response = requests.get(image_url)
with open("image.jpg", "wb") as f:
    f.write(response.content)
