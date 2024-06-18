import requests

def fetch_and_display_inventory():
    access_token = "616MeuZTOLGUUfhh4S7PB39h7T0L3iRLZAYiL1pu"  # Replace with your actual access token
    url = "https://vmpay.vertitecnologia.com.br/api/v1/storables"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            product_name = product.get('name', 'Unknown Product')
            inventories = product.get('inventories', [])
            total_quantity = sum(inventory.get('total_quantity', 0) for inventory in inventories)
            print(f"Product Name: {product_name}, Total Stock: {total_quantity}")
    else:
        print(f"Failed to fetch inventory: {response.status_code}")

if __name__ == "__main__":
    fetch_and_display_inventory()
