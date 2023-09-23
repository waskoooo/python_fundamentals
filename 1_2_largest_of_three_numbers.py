first_n = int(input())
second_n = int(input())
third_n = int(input())

if first_n > second_n > third_n:
    print(first_n)
elif second_n > first_n > third_n:
    print(second_n)
else:
    print(third_n)
