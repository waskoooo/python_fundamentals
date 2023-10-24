chat = []

while True:
    command = input()
    if command == "end":
        break

    words = command.split()

    if words[0] == "Chat":
        chat.append(words[1])
    elif words[0] == "Delete":
        if words[1] in chat:
            chat.remove(words[1])
    elif words[0] == "Edit":
        if words[1] in chat:
            chat[chat.index(words[1])] = words[2]
    elif words[0] == "Pin":
        if words[1] in chat:
            chat.append(chat.pop(chat.index(words[1])))
    elif words[0] == "Spam":
        chat.extend(words[1:])

for message in chat:
    print(message)
