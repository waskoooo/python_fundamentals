# find the capitals

word = input()

capitals = []

for index , char in enumerate(word):
    if char.isupper():
        capitals.append(index)

print(capitals)