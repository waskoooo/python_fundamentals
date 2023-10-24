# Read the initial schedule of lessons and exercises
schedule = input().split(", ")


# Define a function to check if a lesson or exercise already exists in the schedule
def exists(item):
    return item in schedule or any(item in lesson for lesson in schedule)


# Define a function to get the index of a lesson or exercise in the schedule
def index(item):
    return next((i for i, lesson in enumerate(schedule) if item in lesson), -1)


# Process the commands until "course start" is received
while True:
    command = input()
    if command == "course start":
        break

    if command.startswith("Add:"):
        lesson = command[4:]
        if not exists(lesson):
            schedule.append(lesson)

    elif command.startswith("Insert:"):
        lesson, idx = command[7:].split(":")
        idx = int(idx)
        if not exists(lesson):
            schedule.insert(idx, lesson)

    elif command.startswith("Remove:"):
        lesson = command[7:]
        if exists(lesson):
            idx = index(lesson)
            if idx + 1 < len(schedule) and schedule[idx + 1].endswith("-Exercise"):
                schedule.pop(idx + 1)
            schedule.pop(idx)

    elif command.startswith("Swap:"):
        lesson1, lesson2 = command[5:].split(":")
        idx1, idx2 = index(lesson1), index(lesson2)
        if idx1 != -1 and idx2 != -1:
            schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]
            if idx1 + 1 < len(schedule) and schedule[idx1 + 1].endswith("-Exercise"):
                schedule[idx1 + 1], schedule[idx2 + 1] = schedule[idx2 + 1], schedule[idx1 + 1]

    elif command.startswith("Exercise:"):
        lesson = command[9:]
        if exists(lesson):
            idx = index(lesson)
            if idx + 1 >= len(schedule) or not schedule[idx + 1].endswith("-Exercise"):
                schedule.insert(idx + 1, f"{lesson}-Exercise")
        else:
            schedule.append(lesson)
            schedule.append(f"{lesson}-Exercise")

# Print the whole course schedule
for i, lesson in enumerate(schedule):
    print(f"{i + 1}.{lesson}")
