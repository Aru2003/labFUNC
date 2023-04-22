def calculate_shipping_cost(street_name, product_price):
    if street_name in ["Аль-Фараби", "Саина", "Ташенова", "Достык"]:
        if product_price < 10000:
            return 500
        else:
            return 0
    else:
        if product_price < 10000:
            return 1000
        else:
            return 1000
            
            
street_name=str(input("street_name:"))
product_price=int(input("product_price:"))
shipping_cost = calculate_shipping_cost(street_name, product_price)
print("Стоимость доставки: ", shipping_cost, "тг")