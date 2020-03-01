matrix = [[4, 5, 6, 8],
          [1, 4, 0, 6],
          [5, 6, 9, 3]
          ]
summ = 0
num = 0
count = 0
for i in matrix:
    for j in i:
        summ += j
        num += 1
average = summ/num
for indexi, i in enumerate(matrix):
    for indexj, j in enumerate(i):
        if j > average and (indexj + indexi) % 2 == 0:
            count += 1
print(count)
