number = input().split()
inverted = []

for num in number:
    current_number = -int(num)
    inverted.append(current_number)
print(inverted)