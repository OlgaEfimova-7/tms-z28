mx = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
      ]
for indexi, i in enumerate(mx):
    for indexj, j in enumerate(i):
        if indexj > indexi:
            i[indexj] = 0
print(f'Task № 6.9: {mx}')

for indexi, i in enumerate(mx):
    for indexj, j in enumerate(i):
        if indexj < indexi:
            i[indexj] = 0
print(f'Task № 6.10: {mx}')

from random import randint
matrix_a = [[randint(1, 9) for j in range(3)] for i in range(3)]
matrix_b = [[randint(1, 9) for j in range(3)] for i in range(3)]
print(f'Task № 6.11:\n matrix a:{matrix_a}\n matrix b:{matrix_b}')

matrix_c = []
for indexi, i in enumerate(matrix_a):
    list_of_matrix = []
    for indexj, j in enumerate(i):
        list_of_matrix.append(j+matrix_b[indexi][indexj])
    matrix_c.append(list_of_matrix)
print(f'Task № 6.12:\n sum of matrix:{matrix_c}')

matrix_d = []
for indexi, i in enumerate(matrix_a):
    list_of_matrix = []
    for indexj, j in enumerate(i):
        list_of_matrix.append(j-matrix_b[indexi][indexj])
    matrix_d.append(list_of_matrix)
print(f'Task № 6.13:\n difference of matrix:{matrix_d}')

entered_number = int(input('Task № 6.14\n Enter the number: '))
matrix_e = [[j*entered_number for j in i] for i in matrix_a]
print(f'matrix a multiplication by number: {matrix_e}')
