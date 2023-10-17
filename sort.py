# Take input from the user
numbers = input()

numbers_list = numbers.split()

numbers_int = [int(x) for x in numbers_list]

sorted_numbers = sorted(numbers_int)

print(sorted_numbers)
