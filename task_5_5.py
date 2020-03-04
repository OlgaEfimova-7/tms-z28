list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 5, 6, 9, 4]
sorted_list = sorted(list_of_numbers, reverse=True)
for i in list_of_numbers:
    if i % 2 == 0:
        list_of_numbers[list_of_numbers.index(i)] = sorted_list[0]
print(list_of_numbers)

