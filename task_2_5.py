entered_str = input('Please enter the text :')
list_with_entered_string = list(entered_str)
result_str = ''.join(list_with_entered_string[::2])
print(result_str)
