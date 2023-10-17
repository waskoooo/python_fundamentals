def check_palindromes(numbers):
    numbers_list = numbers.split(", ")
    for num_str in numbers_list:
        is_palindrome = num_str == num_str[::-1]
        print(is_palindrome)


numbers = input()
check_palindromes(numbers)
