from math import pi
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return (((self.x - other.x) ** 2 +
                 (self.y - other.y) ** 2) ** (1/2))


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass


class Circle(Figure):
    def __init__(self, coordinates, radius_length):
        self.coordinates = isinstance(coordinates, Point)
        self.radius_length = radius_length

    def perimeter(self):
        return 2 * pi * self.radius_length

    def square(self):
        return pi * self.radius_length ** 2


class Triangle(Figure):
    def __init__(self, first_point, second_point, third_point):
        self.first_point = isinstance(first_point, Point)
        self.second_point = isinstance(second_point, Point)
        self.third_point = isinstance(third_point, Point)
        self.first_side = first_point - second_point
        self.second_side = second_point - third_point
        self.third_side = first_point - third_point

    def perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def square(self):
        half_perim = self.perimeter()/2
        return ((half_perim * (half_perim - self.first_side) *
                (half_perim - self.second_side) *
                (half_perim - self.third_side)) ** (1/2))


class Square(Figure):
    def __init__(self, first_point, second_point):
        self.first_point = isinstance(first_point, Point)
        self.second_point = isinstance(second_point, Point)
        self.side = first_point - second_point

    def perimeter(self):
        return self.side * 4

    def square(self):
        return self.side ** 2
