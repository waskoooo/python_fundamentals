n = int(input())
students = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

# Filter students with an average grade higher than or equal to 4.50
filtered_students = {name: grades for name, grades in students.items() if sum(grades) / len(grades) >= 4.50}

# Print the final dictionary with students and their average grade
for name, average_grade in filtered_students.items():
    average_grade = sum(average_grade) / len(average_grade)
    print(f"{name} -> {average_grade:.2f}")
