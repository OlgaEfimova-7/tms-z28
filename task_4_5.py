first_num, second_num = 0, 1
print(first_num)
print(second_num)
i = 0
num = 0
result_num = second_num
result_num2 = 0
while i < 13:
    result_num2 = result_num + num
    num = result_num
    result_num = result_num2
    print(result_num2)
    i += 1
