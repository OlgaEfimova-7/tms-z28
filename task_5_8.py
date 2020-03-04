entered_string = input('Please enter the sentence: ')
list_of_entered_string = entered_string.split()
result_list = list_of_entered_string[::-1]
result_string = ' '.join(result_list)
print(result_string)
