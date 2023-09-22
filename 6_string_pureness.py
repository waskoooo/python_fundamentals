n = int(input())

for _ in range(n):
    string = input()
    is_pure = all(char not in string for char in ",._")

    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")