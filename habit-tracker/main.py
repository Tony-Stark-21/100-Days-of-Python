import requests
import os
from datetime import datetime
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url= pixela_endpoint, json=users_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph1",
    "name": "Efootball Graph",
    "unit": "Hours",
    "type": "float",
    "color": "momiji",
}

header  ={
    "X-USER-TOKEN" : TOKEN,
}

# response  = requests.post(graph_endpoint, json=graph_configuration, headers=header)
# print(response.text)

today = datetime(year=2026,month=10,day=4)
post_graph_config  = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you play efootball for today? "),
}
graph_id_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# response  = requests.post(url=graph_id_endpoint, json=post_graph_config, headers=header)
# print(response.text)
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
put_config = {
    "quantity": input("How many hours did you play efootball for today? ")
}

# response = requests.put(put_endpoint, json=put_config, headers=header)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(delete_endpoint, headers=header)
print(response.text)
