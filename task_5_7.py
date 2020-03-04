matrix = [[1, 2, 3],
          [6, 5, 3],
          [2, 5, 3]
          ]
count = 0
for i in matrix:
    list_of_i = sorted(i, reverse=True)
    elem_with_0_index = list_of_i[0]
    for indexj, j in enumerate(i):
        if j >= elem_with_0_index:
            i[count], i[indexj] = i[indexj], i[count]
    count += 1
print(matrix)
