entered_string = input('Please enter string:\n')
central_symbol = entered_string[int(len(entered_string) / 2)]
print(central_symbol)
if central_symbol == entered_string[0]:
    new_string = entered_string[1:-1]
    print(new_string)
