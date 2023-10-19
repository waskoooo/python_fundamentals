happiness = input()
factor = float(input())

happiness_list = happiness.split()

happiness_int = [int(x) for x in happiness_list]

happiness_multiplied = [x * factor for x in happiness_int]

average_happiness = sum(happiness_multiplied) / len(happiness_multiplied)

happy_count = sum(x >= average_happiness for x in happiness_multiplied)

total_count = len(happiness_multiplied)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
