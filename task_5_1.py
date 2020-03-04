while True:
    first_operand = input('Please enter first number: ')
    second_operand = input('Please enter second number: ')
    first_number = int(first_operand)
    second_number = int(second_operand)
    sign = input('Please enter the sign: ')
    if sign == '+':
        print(first_number + second_number)
    elif sign == '-':
        print(first_number - second_number)
    elif sign == '*':
        print(first_number * second_number)
    elif sign == '/' and second_number != 0:
        print(first_number / second_number)
    elif sign == '/' and second_number == 0:
        print('nol division')
    elif sign == '0':
        break
    else:
        print('wrong sign')
