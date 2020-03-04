entered_number = int(input('Please enter the number:'))
result = 0
for i in list(range(1, entered_number+1)):
    result += 1 / i
print(result)
