from functools import reduce


def fact2(number):
    """
    :param number: entered number
    :return: double factorial of the number
    """
    if number % 2 != 0:
        return reduce(lambda x, y: x * y, range(1, number+1, 2))
    else:
        return reduce(lambda x, y: x*y, range(2, number+1, 2))


print(fact2(4))
print(fact2(5))
print(fact2(6))
print(fact2(7))
print(fact2(8))
