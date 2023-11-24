def process_string(s):
    total_sum = 0

    i = 0
    while i < len(s):
        # Find the number in the current string
        while i < len(s) and not s[i].isdigit():
            i += 1
        start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        end = i

        if start < end:
            number = int(s[start:end])

            # Process the letter before the number
            if start > 0 and s[start - 1].isalpha():
                char_before = s[start - 1]
                if char_before.isupper():
                    number /= (ord(char_before) - ord('A') + 1)
                else:
                    number *= (ord(char_before) - ord('a') + 1)

            # Process the letter after the number
            if end < len(s) and s[end].isalpha():
                char_after = s[end]
                if char_after.isupper():
                    number -= (ord(char_after) - ord('A') + 1)
                else:
                    number += (ord(char_after) - ord('a') + 1)

            total_sum += number

    return total_sum

# Read input and process each string
input_strings = input().split()
result = sum(process_string(s) for s in input_strings)

# Print the result formatted to the second decimal place
print(f'{result:.2f}')
