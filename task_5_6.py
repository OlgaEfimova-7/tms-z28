list_of_numbers = [1, 2, 5, 6, 8, 7, 9, 10, 11]
count = 0
additional_variable = list_of_numbers[0]
for i in list_of_numbers:
    if i > additional_variable:
        count += 1
    additional_variable = i
print(count)
