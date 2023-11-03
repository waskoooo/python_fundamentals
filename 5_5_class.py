class Class:
    __student_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name:str, grade: float) -> None:
        if Class.__student_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average(self):
        average_grade = sum(self.grades) / len(self.students)
        return float(f"{average_grade:s2f}")

    def __repr__(self):
        students = ", ".join(self.students)
        average_grade = self.get_average()
        return f"The students in {self.name}: {students}. Average grade: {average_grade}"


a_class = Class("118")
a_class.add_student("Peter", 4.88)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
