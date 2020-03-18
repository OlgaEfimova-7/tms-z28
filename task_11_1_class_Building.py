class Building:
    def __init__(self, district=None, age_of_building=None, number_of_apartments_for_sale=None):
        self.__district = district
        self.__age_of_building = age_of_building
        self.__number_of_apartments_for_sale = number_of_apartments_for_sale

    @property
    def district(self):
        return self.__district

    @district.setter
    def district(self, district):
        self.__district = district

    @property
    def age_of_building(self):
        return self.__age_of_building

    @age_of_building.setter
    def age_of_building(self, age_of_building):
        self.__age_of_building = age_of_building

    @property
    def number_of_apartments_for_sale(self):
        return self.__number_of_apartments_for_sale

    @number_of_apartments_for_sale.setter
    def number_of_apartments_for_sale(self, number_of_apartments_for_sale):
        self.__number_of_apartments_for_sale = number_of_apartments_for_sale

    def apartment_purchase(self):
        if self.number_of_apartments_for_sale > 0:
            self.number_of_apartments_for_sale -= 1
        if self.number_of_apartments_for_sale <= 0:
            print('All apartments are sold')

    def lifetime_of_building(self):
        if self.__age_of_building < 0:
            print('Wrong age!')
        elif self.__age_of_building < 25:
            print('Everything is OK')
        elif self.__age_of_building < 70:
            print('Major repairs require')
        else:
            print('Dangerous!!! house may collapse')


building1 = Building()
building1.district = 'Central'
building1.age_of_building = 10
building1.number_of_apartments_for_sale = 4
print(building1.district)
print(building1.age_of_building)
building1.apartment_purchase()
print(building1.number_of_apartments_for_sale)
building1.apartment_purchase()
print(building1.number_of_apartments_for_sale)
building1.apartment_purchase()
print(building1.number_of_apartments_for_sale)
building1.apartment_purchase()
print(building1.number_of_apartments_for_sale)
building1.apartment_purchase()
print(building1.number_of_apartments_for_sale)
building1.lifetime_of_building()
