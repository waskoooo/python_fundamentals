def is_special_number(number):
    # Calculate the sum of digits in the number
    digit_sum = sum(int(digit) for digit in str(number))

    # Check if the sum of digits is 5, 7, or 11
    return digit_sum in [5, 7, 11]


# Input the integer n
n = int(input())

# Iterate through the numbers in the range [1, n]
for number in range(1, n + 1):
    # Check if the number is special
    special = is_special_number(number)

    # Print the number and whether it is special or not
    print(f"{number} -> {special}")