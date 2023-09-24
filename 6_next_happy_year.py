def is_happy_year(year):
    # Convert the year to a string to check for distinct digits
    year_str = str(year)

    # Use a set to store the unique digits in the year
    unique_digits = set()

    # Iterate through each digit in the year
    for digit in year_str:
        # If the digit is already in the set, it's not a happy year
        if digit in unique_digits:
            return False
        # Otherwise, add it to the set
        unique_digits.add(digit)

    # If all digits are distinct, it's a happy year
    return True


def find_next_happy_year(year):
    # Start searching for the next happy year after the given year
    year += 1
    while True:
        if is_happy_year(year):
            return year
        year += 1


# Input the integer year
year = int(input(""))

# Find and print the next happy year
next_happy_year = find_next_happy_year(year)
print(f"{next_happy_year}")