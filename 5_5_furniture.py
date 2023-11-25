import re

purchases = []
total_cost = 0
furniture_dict = {}

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)", line)
    if match:
        name = match.group("name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))

        total_cost += price * quantity

        if name not in furniture_dict:
            furniture_dict[name] = 0

        furniture_dict[name] += price * quantity

print("Bought furniture:")
for name, cost in furniture_dict.items():
    print(f"{name}")
print(f"Total money spend: {total_cost:.2f}")
