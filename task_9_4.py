def change_order_of_args(func):
    def wrapper(*args):
        return args[::-1]
    return wrapper


@change_order_of_args
def function_with_arguments(*args):
    return args


print(function_with_arguments(1, 2, 3, 4, 5))
