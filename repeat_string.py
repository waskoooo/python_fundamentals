word = input().split(" ")
result = ""
for words in word:
    lenght = len(words)
    result += words * lenght
print(result)