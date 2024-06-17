from datetime import datetime, timedelta
from api import get_sales, get_categories
from analysis import analyze_sales_data
from projection import project_inventory

def fetch_and_analyze_sales(category_id, access_token):
    today = datetime.now()
    two_months_ago = today - timedelta(days=60)
    last_year_same_month_start = today.replace(year=today.year - 1, day=1)
    last_year_same_month_end = last_year_same_month_start.replace(month=today.month + 1) - timedelta(days=1)

    sales_last_two_months = get_sales(category_id, two_months_ago, today, access_token)
    sales_last_year_same_month = get_sales(category_id, last_year_same_month_start, last_year_same_month_end, access_token)

    if sales_last_two_months and sales_last_year_same_month:
        sales_analysis_last_two_months = analyze_sales_data(sales_last_two_months)
        sales_analysis_last_year_same_month = analyze_sales_data(sales_last_year_same_month)
        return sales_analysis_last_two_months, sales_analysis_last_year_same_month
    else:
        return None, None

def main(category_id=None, access_token=None):
    if not access_token:
        raise ValueError("Access token is required")

    sales_analysis_last_two_months, sales_analysis_last_year_same_month = fetch_and_analyze_sales(category_id, access_token)

    if sales_analysis_last_two_months is None or sales_analysis_last_year_same_month is None:
        print("Failed to fetch or analyze sales data")
        return {}, get_categories(access_token)  # Empty projection, but still fetch categories

    projection_period = 15
    inventory_projection = project_inventory(sales_analysis_last_two_months, projection_period)

    # Ordenar os dados por quantidade projetada, do maior para o menor
    sorted_projection = dict(sorted(inventory_projection.items(), key=lambda item: item[1], reverse=True))

    categories = get_categories(access_token)
    return sorted_projection, categories  # Retornando os dados ordenados

if __name__ == "__main__":
    main()
