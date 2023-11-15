phone_book = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone_number = entry.split("-")
    phone_book[name] = phone_number

searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phone_book.keys():
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(F"Contact {searched_name} does not exist.")