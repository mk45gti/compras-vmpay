from flask import Flask, render_template, request
import requests
from main import main

app = Flask(__name__)

def fetch_inventory(access_token):
    url = "https://vmpay.vertitecnologia.com.br/api/v1/storables"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)
    inventory = {}

    if response.status_code == 200:
        inventory_data = response.json()
        # Verificar e extrair informações com segurança
        for item in inventory_data:
            item_id = item.get('id')
            total_quantity = item.get('total_quantity')
            committed_quantity = item.get('committed_quantity')

            if item_id is not None and total_quantity is not None and committed_quantity is not None:
                inventory[item_id] = total_quantity - committed_quantity
            else:
                # Logar itens que estão faltando dados necessários
                print(f"Missing data for item {item_id}: total_quantity or committed_quantity is missing.")
    else:
        print(f"Failed to fetch inventory, status code: {response.status_code}, response: {response.text}")

    return inventory


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    access_token = "616MeuZTOLGUUfhh4S7PB39h7T0L3iRLZAYiL1pu"
    category_id = request.args.get('category_id')
    projection, categories = main(category_id, access_token)
    print(f"Projection: {projection}")
    inventory = fetch_inventory(access_token)
    print(f"Inventory: {inventory}")

    for product_id, details in projection.items():
        stock = inventory.get(product_id, 0)
        if isinstance(details, dict):
            quantity = details.get('quantity', 0)
        else:
            print(f"Unexpected type for details: {type(details)}, expected dict.")
            quantity = 0
        projection[product_id] = {'quantity': quantity, 'stock': stock}
        print(f"Product ID: {product_id}, Quantity: {quantity}, Stock: {stock}")

    return render_template('dashboard.html', projection=projection, categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
