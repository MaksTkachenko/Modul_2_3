# Створіть клас Circle, який представляє коло. Реалізуйте методи для обчислення
# площі та довжини кола. Використовуйте аттрибут класу для зберігання значення π (pi).

import math

def task_6():

    class Circle:

        pi = math.pi

        def __init__(self, radius):
            self.radius = radius

        def circuit(self):
            return round(2 * self.radius * self.pi, 2)

        def area_circle(self):
            return round(self.pi * self.radius**2, 2)

    radius_input = int(input("Enter the radius of the circle: "))
    circle = Circle(radius_input)
    print(f"Circuit = {circle.circuit()}\nArea of a circle = {circle.area_circle()}cm2")
