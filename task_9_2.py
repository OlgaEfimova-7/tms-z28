function1 = lambda **kwargs: dict(zip(list(key * 2 for key in kwargs.keys()), list(kwargs.values())))
print(function1(a=1, d=2, f=3))

function2 = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(function2(a=1, d=2, f=3))
