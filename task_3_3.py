entered_string = input('Please enter string:\n')
if len(entered_string) > 10:
    new_string = f'{entered_string}!!!'
    print(new_string)
elif len(entered_string) < 10:
    print(entered_string[1])
