import requests

def test_fetch_inventory():
    access_token = "616MeuZTOLGUUfhh4S7PB39h7T0L3iRLZAYiL1pu"  # Substitua pelo token real
    url = "https://vmpay.vertitecnologia.com.br/api/v1/storables"
    params = {
        "access_token": access_token
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        inventory_data = response.json()
        for product in inventory_data:
            product_name = product.get('name')
            inventory = product.get('inventories')
            if inventory and 'total_quantity' in inventory[0]:
                stock_quantity = inventory[0].get('total_quantity')  # 'total_quantity' é o campo que contém a quantidade em estoque
            else:
                stock_quantity = 'No stock information'
            print(f"Product Name: {product_name}, Stock Quantity: {stock_quantity}")
    else:
        print(f"Failed to fetch inventory, status code: {response.status_code}, response: {response.text}")

if __name__ == "__main__":
    test_fetch_inventory()