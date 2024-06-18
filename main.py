from api import get_categories, get_sales, fetch_inventory
from datetime import datetime, timedelta

def main(category_id, access_token):
    start_date = datetime.now() - timedelta(days=30)  # Adjust according to your needs
    end_date = datetime.now()
    sales_data = get_sales(category_id, start_date, end_date, access_token) if category_id else []
    projection = {item['id']: item for item in sales_data}  # Adjust this according to your actual projection logic
    inventory = fetch_inventory(access_token)
    categories = get_categories(access_token)
    return projection, inventory, categories
