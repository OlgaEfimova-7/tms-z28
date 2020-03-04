list_of_numbers_in_range = list(range(200, 301))
list_of_dividers = []
for number in list(range(200, 300+1)):
    summ_of_dividers = 0
    for i in list(range(1, number)):
        if number % i == 0:
            summ_of_dividers += i
    list_of_dividers.append(summ_of_dividers)
for indexi, i in enumerate(list_of_numbers_in_range):
    for indexj, j in enumerate(list_of_dividers):
        if list_of_numbers_in_range[indexi] == j and list_of_dividers[indexi] == list_of_numbers_in_range[indexj]:
            final_tuple = (i, list_of_dividers[indexi])
print(final_tuple)
