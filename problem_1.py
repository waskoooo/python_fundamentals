budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

cost_flour = price_flour * (students - students // 5)

cost_eggs = price_egg * 10 * students

cost_aprons = price_apron * ((students * 120 + 99) // 100)

total_cost = cost_flour + cost_eggs + cost_aprons

if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")
