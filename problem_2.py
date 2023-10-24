sequence = input().split()
commands = []

while True:
    command = input()
    if command == "Finish":
        break
    commands.append(command)

for command in commands:
    if "Add" in command:
        _, value = command.split()
        sequence.append(value)
    elif "Remove" in command:
        _, value = command.split()
        if value in sequence:
            sequence.remove(value)
    elif "Replace" in command:
        _, value, replacement = command.split()
        if value in sequence:
            sequence[sequence.index(value)] = replacement
    elif "Collapse" in command:
        _, value = command.split()
        sequence = [num for num in sequence if int(num) >= int(value)]

print(" ".join(sequence))
