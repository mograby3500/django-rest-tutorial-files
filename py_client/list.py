import requests

endpoint = "http://localhost:8000/api/products/list/"

data = {"title": "API created Product :D", "price": 32.99}

get_reponse = requests.get(endpoint)
print(get_reponse.json())
