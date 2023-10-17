def all_char(first: str,second: str) -> list:
    characters = []
    for current_character_as_digit in range(ord(first)+1, ord(second)):
        characters.append((chr(current_character_as_digit)))
    return characters


first_character = input()
second_character = input()
final_result = all_char(first_character , second_character)
print(" ".join(final_result))
