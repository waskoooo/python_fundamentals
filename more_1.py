# find the largest

number = input()
largest_number = ''.join(sorted(number, reverse=True))
largest_number = int(largest_number)
print(largest_number)