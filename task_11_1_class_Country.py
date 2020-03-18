import csv


class Country:
    def __init__(self, name=None, currency=None, population=None):
        self.__name = name
        self.__currency = currency
        self.__population = population

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    def capital(self):
        with open('capitals.csv', 'r') as my_file:
            csv_reader = csv.reader(my_file)
            field = next(csv_reader)
            capital = None
            for rows in csv_reader:
                for index, row in enumerate(rows):
                    if index == 0 and self.__name == row:
                        capital = (rows[1])
                        break
        return capital

    def birth_of_new_person(self):
        self.__population += 1


country1 = Country()
country1.name = 'Belarus'
country1.currency = 'BYN'
country1.population = 9413446
print(country1.name)
print(country1.currency)
print(country1.population)
print(country1.capital())
country1.birth_of_new_person()
country1.birth_of_new_person()
country1.birth_of_new_person()
country1.birth_of_new_person()
print(country1.population)
