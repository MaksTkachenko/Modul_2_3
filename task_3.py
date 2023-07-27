# Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути,
# такі як назва, швидкість і вартість. Реалізуйте метод __gt__, який порівнює два
# транспортних засоби за швидкістю. Створіть список транспортних засобів і
# відсортуйте його за швидкістю.


def task_3():

    class Vehicle:

        def __init__(self, brand_car, speed_car, cost_car):
            self.brand_car = brand_car
            self.speed_car = speed_car
            self.cost_car = cost_car

        def get_info(self):
            """A method that outputs information"""
            return f"This ia {self.brand_car}, Max. speed {self.speed_car} km/h, cost {self.cost_car}$"

        def __gt__(self, other):
            return self.speed_car > other.speed_car

    car_1 = Vehicle("BMW", 250, 32000)
    car_2 = Vehicle("AUDI", 220, 35000)
    car_3 = Vehicle("Volkswagen", 200, 20000)
    car_4 = Vehicle("Porch", 310, 250000)

    cars = [car_1, car_2, car_3, car_4]

    sorted_cars_speed = sorted(cars)

    for car in sorted_cars_speed:
        print(f"{car.brand_car} - Speed: {car.speed_car} km/h - Cost: ${car.cost_car}")
