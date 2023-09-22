divisor = int(input())
bound = int(input())
largest_int = 0
for i in range(1, bound + 1):
    if i % divisor == 0:
        largest_int = i

if largest_int > 0:
    print(largest_int)