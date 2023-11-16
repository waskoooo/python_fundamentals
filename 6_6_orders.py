products = {}

while True:
    input_line = input()
    if input_line == "buy":
        break

    product_info = input_line.split()
    product_name = product_info[0]
    product_price = float(product_info[1])
    product_quantity = int(product_info[2])

    if product_name not in products:
        products[product_name] = {'price': product_price, 'quantity': product_quantity}
    else:
        products[product_name]['quantity'] += product_quantity
        if products[product_name]['price'] != product_price:
            products[product_name]['price'] = product_price

for product_name, product_data in products.items():
    total_price = product_data['price'] * product_data['quantity']
    print(f"{product_name} -> {total_price:.2f}")
