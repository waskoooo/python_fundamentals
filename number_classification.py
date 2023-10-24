numbers = input()

numbers_list = numbers.split(", ")

numbers_int = [int(x) for x in numbers_list]

positive_numbers = [num for num in numbers_int if num >= 0]
negative_numbers = [num for num in numbers_int if num < 0]
even_numbers = [num for num in numbers_int if num % 2 == 0]
odd_numbers = [num for num in numbers_int if num % 2 != 0]

print("Positive:", ', '.join(map(str, positive_numbers)))
print("Negative:", ', '.join(map(str, negative_numbers)))
print("Even:", ', '.join(map(str, even_numbers)))
print("Odd:", ', '.join(map(str, odd_numbers)))
