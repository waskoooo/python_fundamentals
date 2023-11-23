message = input()
encrypted_message = ""

for char in message:
    encrypted_char = chr(ord(char) + 3)
    encrypted_message += encrypted_char
print(encrypted_message)