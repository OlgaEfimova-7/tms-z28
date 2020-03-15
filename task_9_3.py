def remov_of_even_elements(func):
    def wrapper(list_of_numbers):
        return func(list(filter(lambda x: x % 2 != 0, list_of_numbers)))
    return wrapper


@remov_of_even_elements
def funct_that_takes_list_of_numbers(list_of_numbers):
    return list_of_numbers


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(funct_that_takes_list_of_numbers(a))

