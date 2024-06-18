from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = 'JtC4OK3au5cW9wVxrRrZOD26LcTOCyHwHvwQEZ0i'

def get_categories(access_token):
    url = f"https://vmpay.vertitecnologia.com.br/api/v1/categories?access_token={access_token}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_inventory(access_token, category_id=None):
    """Fetch the inventory and process it to calculate stock."""
    url = f"https://vmpay.vertitecnologia.com.br/api/v1/storables?access_token={access_token}"
    if category_id:
        url += f"&category_id={category_id}"
    response = requests.get(url)
    inventory = {}
    if response.status_code == 200:
        data = response.json()
        print(f"Data received for category")  # Log what data is received
        for product in data:
            product_id = product['id']
            total_stock = sum(item['total_quantity'] for item in product['inventories'] if 'total_quantity' in item)
            inventory[product_id] = {'name': product['name'], 'stock': total_stock}
        return inventory
    else:
        print("Failed to fetch inventory:", response.status_code, response.text)
        return {}

@app.route('/', methods=['GET'])
def dashboard():
    category_id = request.args.get('category_id')
    categories = get_categories(ACCESS_TOKEN)
    print(f"Categories loaded")  # Check what categories are loaded
    inventory = get_inventory(ACCESS_TOKEN, category_id) if category_id else {}
    print(f"Inventory loaded for category")  # Check inventory loaded
    return render_template('dashboard.html', categories=categories, inventory=inventory, selected_category=category_id)



if __name__ == '__main__':
    app.run(debug=True)
