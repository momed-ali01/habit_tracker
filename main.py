import requests
from datetime import datetime as dt

USERNAME = "momedali"
GRAPH_ID = "graph1"
TOKEN = "cleqibz8KJBVcu5bjuo4H"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Duolingo Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

yesterday = dt(year=2024, month=8, day=22).strftime("%Y%m%d")
today = dt.today().strftime("%Y%m%d")

pixel_creation_config = {
    "date": today,
    "quantity": "1120"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{today}"

update_config = {
    "quantity": "800"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{yesterday}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
