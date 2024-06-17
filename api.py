import requests
from datetime import datetime, timedelta

def get_sales(category_id, start_date, end_date, access_token):
    url = "https://vmpay.vertitecnologia.com.br/api/v1/vends"
    params = {
        "category_id": category_id,
        "start_date": start_date.strftime("%Y-%m-%d %H:%M:%S"),  # Ajustando o formato de data conforme necessário
        "end_date": end_date.strftime("%Y-%m-%d %H:%M:%S"),
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code, response.text)  # Imprime erro
        return None

def fetch_sales_data(category_id, access_token):
    today = datetime.now()
    two_months_ago = today - timedelta(days=60)
    last_year_same_month_start = today.replace(year=today.year - 1, day=1)
    last_year_same_month_end = last_year_same_month_start.replace(month=today.month + 1) - timedelta(days=1)

    sales_last_two_months = get_sales(category_id, two_months_ago, today, access_token)
    sales_last_year_same_month = get_sales(category_id, last_year_same_month_start, last_year_same_month_end, access_token)

    return sales_last_two_months, sales_last_year_same_month

def get_categories(access_token):
    url = "https://vmpay.vertitecnologia.com.br/api/v1/categories"
    params = {
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        categories = response.json()
        return categories
    else:
        return []



