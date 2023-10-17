def find_min_max_sum(numbers):
    numbers_list = numbers.split()

    numbers_int = [int(x) for x in numbers_list]

    min_number = min(numbers_int)
    max_number = max(numbers_int)
    sum_number = sum(numbers_int)

    return min_number, max_number, sum_number


numbers = input()
min_number, max_number, sum_numbers = find_min_max_sum(numbers)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
