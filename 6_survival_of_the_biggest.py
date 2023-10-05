numbers = input().split()
n = int(input())
numbers = [int(x) for x in numbers]

for i in range(n):
    numbers.remove(min(numbers))

numbers = [str(x) for x in numbers]

result = ", ".join(numbers)
print(result)