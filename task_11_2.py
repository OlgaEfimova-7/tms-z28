class Car:
    def __init__(self, brand=None, model=None, year_of_manufacture=None, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_of_manufacture = year_of_manufacture
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture

    @year_of_manufacture.setter
    def year_of_manufacture(self, year_of_manufacture):
        self.__year_of_manufacture = year_of_manufacture

    # method showing speed of the car
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def turn(self):
        self.__speed = -self.__speed


car1 = Car()
car1.brand = 'Mercedes'
car1.model = 'A-Class'
car1.year_of_manufacture = '2019'
car1.speed = 60
print(car1.brand)
print(car1.model)
print(car1.year_of_manufacture)
print(car1.speed)
car1.increase_speed()
car1.increase_speed()
car1.increase_speed()
car1.increase_speed()
print(car1.speed)
car1.decrease_speed()
print(car1.speed)
car1.turn()
print(car1.speed)
car1.stop()
print(car1.speed)
