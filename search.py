number = int(input())
word = input()
strings = []

for num in range(number):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range(len(strings) -1 , -1 , -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)