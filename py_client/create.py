import requests

endpoint = "http://localhost:8000/api/products/create/"

data = {"title": "Slave", "content": "White slave", "price": 1}

get_reponse = requests.post(endpoint, json=data)
print(get_reponse.json())
