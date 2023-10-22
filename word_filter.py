text = input()

words = text.split()

even_words = [word for word in words if len(word) % 2 == 0]

for word in even_words:
    print(word)
