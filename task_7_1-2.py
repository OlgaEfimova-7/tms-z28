def centimetres_from_inches(a):
    """
    :param a: inches
    :return: centimetres
    """
    return a * 2.54


def inches_from_centimetres(a):
    """
    :param a: centimetres
    :return: inches
    """
    return a / 2.54


def kilometers_from_miles(a):
    """
    :param a: miles
    :return: kilometres
    """
    return a * 1.609


def miles_from_kilometers(a):
    """

    :param a: kilometres
    :return: miles
    """
    return a / 1.609


def kilos_from_pounds(a):
    """
    :param a: pounds
    :return: kilos
    """
    return a / 2.2046


def pounds_from_kilos(a):
    """
    :param a: kilos
    :return: pounds
    """
    return a * 2.2046


def grams_from_ounces(a):
    """
        :param a: ounces
        :return: grams
        """
    return a / 0.035274


def ounces_from_grams(a):
    """
        :param a: grams
        :return: ounces
        """
    return a * 0.035274


def liters_from_gallons(a):
    """
            :param a: gallons
            :return: liters
            """
    return a * 3.785


def gallons_from_liters(a):
    """
            :param a: liters
            :return: gallons
            """
    return a / 3.785


def liters_from_pints(a):
    """
            :param a: pints
            :return: liters
            """
    return a / 2.113


def pints_from_liters(a):
    """
            :param a: liters
            :return: pints(American)
            """
    return a * 2.113


print('1. Дюймы в сантиметры\n'
      '2. Сантиметры в дюймы\n'
      '3. Мили в километры\n'
      '4. Километры в мили\n'
      '5. Фунты в килограммы\n'
      '6. Килограммы в фунты\n'
      '7. Унции в граммы\n'
      '8. Граммы в унции\n'
      '9. Галлон в литры\n'
      '10. Литры в галлоны\n'
      '11. Пинты в литры\n'
      '12. Литры в пинты\n'
      ' 0 - Выход из программы')
while True:
    entered_number_of_operation = input('Пожалуйста, выберете номер операции:')
    number_of_operation = int(entered_number_of_operation)
    if number_of_operation < 0 or 12 < number_of_operation:
        print('Неверный номер функции')
        continue
    elif number_of_operation == 0:
        break
    entered_num = input('Пожалуйста, введите числовое значение:')
    num = int(entered_num)
    if number_of_operation == 1:
        print(centimetres_from_inches(num))
    elif number_of_operation == 2:
        print(inches_from_centimetres(num))
    elif number_of_operation == 3:
        print(kilometers_from_miles(num))
    elif number_of_operation == 4:
        print(miles_from_kilometers(num))
    elif number_of_operation == 5:
        print(kilos_from_pounds(num))
    elif number_of_operation == 6:
        print(pounds_from_kilos(num))
    elif number_of_operation == 7:
        print(grams_from_ounces(num))
    elif number_of_operation == 8:
        print(ounces_from_grams(num))
    elif number_of_operation == 9:
        print(liters_from_gallons(num))
    elif number_of_operation == 10:
        print(gallons_from_liters(num))
    elif number_of_operation == 11:
        print(liters_from_pints(num))
    elif number_of_operation == 12:
        print(pints_from_liters(num))
