# Створіть клас Rectangle для представлення прямокутника.
# Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи.

def task_1():

    class Rectangle:

        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area_rectangle(self):
            return self.length * self.width

        def perimeter_rectangle(self):
            return (self.length + self.width) * 2

    leng = int(input("Enter length rectangle: "))
    widt = int(input("Enter width rectangle: "))

    rectangle = Rectangle(leng, widt)

    print(f"The area of the rectangle is {rectangle.area_rectangle()}")
    print(f"The perimeter of the rectangle is equal {rectangle.perimeter_rectangle()}")
