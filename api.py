import requests
from datetime import datetime, timedelta

def get_sales(category_id, start_date, end_date, access_token):
    url = "https://vmpay.vertitecnologia.com.br/api/v1/vends"
    params = {
        "category_id": category_id,
        "start_date": start_date.strftime("%Y-%m-%d %H:%M:%S"),
        "end_date": end_date.strftime("%Y-%m-%d %H:%M:%S"),
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print("Failed to fetch data:", response.status_code, response.text)
        return []

def get_categories(access_token):
    url = "https://vmpay.vertitecnologia.com.br/api/v1/categories"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_response = response.json()
        if 'data' in json_response:
            return json_response['data']
        else:
            return json_response
    else:
        print("Failed to fetch categories:", response.status_code, response.text)
        return []

def fetch_inventory(access_token):
    url = "https://vmpay.vertitecnologia.com.br/api/v1/storables"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    inventory = {}
    if response.status_code == 200:
        products = response.json()
        for product in products:
            product_id = product.get('id')
            total_quantity = sum(item.get('total_quantity', 0) for item in product.get('inventories', []))
            committed_quantity = sum(item.get('committed_quantity', 0) for item in product.get('inventories', []))
            inventory[product_id] = total_quantity - committed_quantity
    else:
        print("Failed to fetch inventory:", response.status_code, response.text)
    return inventory
