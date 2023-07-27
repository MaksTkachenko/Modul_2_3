# Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для
# відстеження кількості студентів. Для цього змінюйте значення атрибуту класу у
# методі __init__ . Та створіть клас метод для виведення загальної кількості студентів.

def task_7():

    class Student:

        def __init__(self, students, course):
            self.students = students
            self.course = course

        @classmethod
        def print_count(cls):
            count = 0
            for i in list_student:
                count += 1
            return f"Total number of students {count}"

    student_1 = Student("Student_1", 3)
    student_2 = Student("Student_2", 4)
    student_3 = Student("Student_3", 1)

    list_student = (student_1, student_2, student_3)

    print(Student.print_count())
