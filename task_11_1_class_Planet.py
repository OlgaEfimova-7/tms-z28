class Planet:
    def __init__(self, name=None, average_surface_temperature=None, number_of_satellites=None):
        self.__name = name
        self.__average_surface_temperature = average_surface_temperature
        self.__number_of_satellites = number_of_satellites

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def average_surface_temperature(self):
        return self.__average_surface_temperature

    @average_surface_temperature.setter
    def average_surface_temperature(self, average_surface_temperature):
        self.__average_surface_temperature = average_surface_temperature

    @property
    def number_of_satellites(self):
        return self.__number_of_satellites

    @number_of_satellites.setter
    def number_of_satellites(self, number_of_satellites):
        self.__number_of_satellites = number_of_satellites

    def order_in_solar_system(self):
        if self.__name == 'Mercury':
            print(1)
        elif self.__name == 'Venus':
            print(2)
        elif self.__name == 'Earth':
            print(3)
        elif self.__name == 'Mars':
            print(4)
        elif self.__name == 'Jupiter':
            print(5)
        elif self.__name == 'Saturn':
            print(6)
        elif self.__name == 'Uranus':
            print(7)
        elif self.__name == 'Neptune':
            print(8)
        else:
            print('it is not a planet of the Solar System')

    def origin_of_name(self):
        if self.__name == 'Mercury':
            print('Названа в честь древнеримского бога торговли – быстроногого Меркурия, '
                  'поскольку она движется по небесной сфере быстрее других планет.')
        elif self.__name == 'Venus':
            print('Получила имя в честь древнеримской богини любви Венеры. ')
        elif self.__name == 'Earth':
            print('Английское Earth возникло от англо-саксонского слова VIII века, обозначавшего землю или грунт. '
                  'Это единственная в Солнечной системе планета с именем, не имеющим отношения к римской мифологии.')
        elif self.__name == 'Mars':
            print('Получила имя в честь древнеримского бога войны Марса')
        elif self.__name == 'Jupiter':
            print('Крупнейшая в Солнечной системе планета названа в честь древнеримского верховного бога-громовержца.')
        elif self.__name == 'Saturn':
            print('Названа в честь бога земледелия Сатур')
        elif self.__name == 'Uranus':
            print('Названа в честь греческого бога неба Урана')
        elif self.__name == 'Neptune':
            print('Большой голубой гигант (этот цвет обусловлен оттенком атмосферы) '
                  'назван в честь римского бога морей. ')
        else:
            print('it is not a planet of the Solar System')


planet1 = Planet()
planet1.name = 'Earth'
planet1.average_surface_temperature = 22
planet1.number_of_satellites = 1
print(planet1.name)
print(planet1.average_surface_temperature)
print(planet1.number_of_satellites)
planet1.order_in_solar_system()
planet1.origin_of_name()