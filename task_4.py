# Створіть клас Student для представлення студента. Додайте атрибути, такі як
# ім'я, прізвище і список оцінок. Реалізуйте метод __len__, який повертає кількість
# оцінок студента. Створіть список студентів і відсортуйте його за кількістю оцінок.


def task_4():

    class Student:

        def __init__(self, name, surname, grades=None):
            self.name = name
            self.surname = surname
            self.grades = grades

        def __len__(self):
            """returns the number of elements in the sequence"""
            return len(self.grades)

        def __repr__(self):
            """returns a printable representation of an object """
            return f"Student {self.name} {self.surname} has the following grades: {self.grades}"

    student_1 = Student("Maksim", "Tkachenko", [10, 7, 9, 11, 11, 8, 9, 12])
    student_2 = Student("Kirill", "Bolib", [10, 7, 6, 8, 8, 12])
    student_3 = Student("Vitali", "Chernykov", [10, 7, 11, 8, 9, 8, 12])

    students = [student_1, student_2, student_3]
    sorted_students = sorted(students, key=lambda student: len(student), reverse=True)

    for stud in sorted_students:
        print(stud)
