list_of_numbers = [1, 2, 5, 6, 8, 7, 9, 10, 11]
count = 0
following_elem = 0
index_of_following_elem = 2
previous_elem = 0
index_of_previous_elem = 0
n = 1
for i in list_of_numbers[1:-1]:
    following_elem = list_of_numbers[index_of_following_elem]
    previous_elem = list_of_numbers[index_of_previous_elem]
    if i > following_elem and i > previous_elem:
        count += 1
    if i < following_elem and index_of_following_elem == len(list_of_numbers)-1:
        count += 1
    index_of_following_elem += 1
    index_of_previous_elem += 1
print(count)
