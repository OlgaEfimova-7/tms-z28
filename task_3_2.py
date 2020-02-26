amount_of_guests = int(input('Please enter amount of guests:\n'))
if amount_of_guests > 50:
    print('restaurant')
elif 20 <= amount_of_guests <= 50:
    print('cafe')
else:
    print('at home')
