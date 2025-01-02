import math


class Circle:
    def __init__(self, radius):
        # __변수 : private
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_circle_area(self):
        return math.pi * (self.__radius**2)

    def get_radius(self):
        return self.__radius


Circle = Circle(10)
# print(Circle.__radius) # AttributeError: 'Circle' object has no attribute '__radius'
print(Circle.get_radius())
print("원 둘레 : ", Circle.get_circumference())
print("원 면적 : ", Circle.get_circle_area())
