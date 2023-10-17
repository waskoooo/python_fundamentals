num_as_string = input().split()
num_as_digits = []
for number in num_as_string:
    num_as_digits.append((int(number)))
is_even = lambda  x: x % 2 == 0
result = list(filter(is_even, num_as_digits))
print(result)
