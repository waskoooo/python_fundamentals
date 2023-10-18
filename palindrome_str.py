words = input().split()
search_palindrome = input()

found_palindromes = [word for word in words if word == word[::-1]]
num_occurrences = found_palindromes.count(search_palindrome)

print(found_palindromes)
print(f"Found palindrome {num_occurrences} times")
