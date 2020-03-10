def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b - d ** (1 / 2)) / (2 * a)
        x2 = (- b + d ** (1 / 2)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = (- b) / (2 * a)
        return x
    else:
        return 'the equation has no real roots'


print(quadratic_equations(a=10, b=12, c=-21))
