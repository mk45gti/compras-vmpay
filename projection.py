def project_inventory(needs, projection_period):
    # Calcular a necessidade de estoque baseada em vendas diárias médias e o período de projeção
    projected_needs = {}
    for product, total_sales in needs.items():
        average_daily_sales = total_sales / projection_period
        projected_needs[product] = average_daily_sales * projection_period
    return projected_needs
