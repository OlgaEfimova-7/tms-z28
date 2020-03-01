first_list = [1, 2, 3, 4, 5]
new_list = []
for index, i in enumerate(first_list):
    new_list.insert(index-1, i)
print(new_list)
