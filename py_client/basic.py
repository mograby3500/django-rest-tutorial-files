import sys

import requests

# endpoint= "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
get_response = requests.post(
    endpoint,
    json={
        "title": None,
        "price": "Heyy",
    },
)

print(get_response.text)
# print(get_response.status_code)
