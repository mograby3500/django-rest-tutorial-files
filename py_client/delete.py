import requests

print("Available Product IDs: ")
products_endpoint = "http://localhost:8000/api/products/list/"
products = requests.get(products_endpoint)


for product in products.json():
    print(product["id"])


product_id = input("Enter the id of the product you want to delete: ")

try:
    product_id = int(product_id)
except:
    print(f"{product_id} is not a valid id")
    product_id = None

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_reponse = requests.delete(endpoint)
    print(get_reponse)
