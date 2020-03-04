for number in list(range(100, 105+1)):
    list_of_dividers = []
    for i in list(range(2, number)):
        if number % i == 0:
            list_of_dividers.append(str(i))
        string_of_dividers = ' '.join(list_of_dividers)
    print(f'{number}: {string_of_dividers}')


