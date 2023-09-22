n = int(input())  # Number of strings to input

for _ in range(n):
    string = input()

    if string != "SoftUni":
        for char in string:
            print(char * 2, end="")

        print() 