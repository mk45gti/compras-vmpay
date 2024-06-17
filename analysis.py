from collections import defaultdict

def analyze_sales_data(sales_data):
    # Dicionário para manter a soma das quantidades de cada produto
    product_sales = defaultdict(int)

    # Analisar os dados de venda
    for sale in sales_data:
        product_name = sale['good']['name']
        quantity_sold = sale['quantity']
        product_sales[product_name] += quantity_sold

    return product_sales
