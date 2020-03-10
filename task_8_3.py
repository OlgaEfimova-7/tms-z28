from functools import reduce


def factorial(number):
    return reduce(lambda x, y: x * y, range(1, number + 1))


def sin1(x, epsilon):
    n = 0
    sin_x = 0
    while abs((-1) ** n * x ** (2 * n + 1) / factorial((2 * n + 1))) > epsilon:
        sin_x += (-1) ** n * x ** (2 * n + 1) / factorial((2 * n + 1))
        n += 1
    return sin_x


print(sin1(1, 0.00000000001))
print(sin1(1, 0.00001))
print(sin1(1, 0.001))
print(sin1(1, 0.01))
print(sin1(1, 0.1))
print(sin1(1, 0.15))
