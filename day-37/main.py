import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_API_TOKEN")
USERNAME = "joeydon"

users_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# How to use requests.post
response = requests.post(url=pixela_endpoint, json=users_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60",
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# How to use requests.put
update_pixel_params = {
    "quantity": "30",
}

update_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
response = requests.put(url=update_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# How to use requests.delete
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
