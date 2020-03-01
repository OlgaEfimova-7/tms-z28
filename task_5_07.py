from random import randint
start_of_the_range = int(input('Please enter the range. Start of the range: '))
end_of_the_range = int(input('end of the range: '))
list_of_range = list(range(start_of_the_range, end_of_the_range))
number_of_attempts = int(input('Please enter the number of attempts: '))
right_number = randint(start_of_the_range, end_of_the_range)
i = 1
while i <= number_of_attempts:
    entered_number = int(input('Please enter your answer: '))
    if entered_number == right_number:
        print('You are the winner')
        break
    elif i == number_of_attempts:
        print(f'You are the loser. Right number is {right_number}')
    elif entered_number > right_number:
        print('Smaller')
    elif entered_number < right_number:
        print('Bigger')
    i += 1
