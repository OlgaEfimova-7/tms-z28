number = 12345
number_digit = 10000
summ_of_nums = 0
product_of_nums = 1
while number_digit >= 1:
    num = number//number_digit
    number = number - number_digit * num
    summ_of_nums += num
    product_of_nums *= num
    number_digit /= 10
print(summ_of_nums)
print(product_of_nums)
