from Lesson13.task_13_2_classes import Math
from Lesson13.task_13_2_exceptions import WrongOperationException
while True:
    try:
        first_number, second_number = int(input('Please enter the first number: ')), \
                                      int(input('Please, enter the second number: '))
    except ValueError:
        print('Wrong arguments: you should enter numbers')
        continue
    while True:
        math = Math(first_number, second_number)
        sign_of_operation = input('please select an operation:\n+\n-\n*\n/\n')
        try:
            if sign_of_operation == '+':
                print(math.addition)
                break
            elif sign_of_operation == '-':
                print(math.subtraction)
                break
            elif sign_of_operation == '*':
                print(math.multiplication)
                break
            elif sign_of_operation == '/':
                print(math.division)
                break
            else:
                raise WrongOperationException('Incorrect operation! Please choice another operation!')
        except WrongOperationException as err:
            print(f'{err}')
