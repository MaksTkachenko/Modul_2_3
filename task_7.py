# Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для
# відстеження кількості студентів. Для цього змінюйте значення атрибуту класу у
# методі __init__ . Та створіть клас метод для виведення загальної кількості студентів.

def task_7():

    class Student:

        count = 0

        def __init__(self, students, course):
            self.students = students
            self.course = course
            Student.count += 1

        @classmethod
        def print_count(cls):
            return f"Total number of students {Student.count}"

    student_1 = Student("Student_1", 3)
    student_2 = Student("Student_2", 4)
    student_3 = Student("Student_3", 1)
    student_4 = Student("Student_4", 2)

    print(Student.print_count())
