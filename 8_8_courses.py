courses = {}

while True:
    input_line = input()
    if input_line == "end":
        break

    course_name, student_name = input_line.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

# Print the information about each course and its registered students
for course_name, registered_students in courses.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
