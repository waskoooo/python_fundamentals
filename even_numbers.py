# Take input from the user
numbers = input()

# Split the input into a list of strings
numbers_list = numbers.split(", ")

# Convert the list of strings into a list of integers
numbers_int = [int(x) for x in numbers_list]

# Find the indices of all even numbers
even_indices = [i for i, num in enumerate(numbers_int) if num % 2 == 0]

# Print the result
print(even_indices)
