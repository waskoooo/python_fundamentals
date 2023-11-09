product_info = input().split()

stock_data = {}

for i in range(0, len(product_info), 2):
    product = product_info[i]
    quantity = int(product_info[i+1])
    stock_data[product] = quantity

products_to_search = input().split()
for new_product in products_to_search:
    if new_product in stock_data:
        print(f"We have {stock_data[new_product]} of {new_product} left")
    else:
        print(f"Sorry, we don\'t have {new_product}")
