import math

first_number = int(input())
second_number = int(input())

factorial_first_number = math.factorial(first_number)
factorial_second_number = math.factorial(second_number)

result = factorial_first_number / factorial_second_number
print(f"{result:.2f}")