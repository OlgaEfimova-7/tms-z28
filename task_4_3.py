dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(dict1):
    new_key = key + str(len(key))
    dict1[new_key] = dict1.get(key)
    del dict1[key]
print(dict1)

dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_of_new_keys = []
list_of_values = []
for key, value in dict1.items():
    new_key = key + str(len(key))
    list_of_new_keys.append(new_key)
    list_of_values.append(value)
dict1 = dict(zip(list_of_new_keys, list_of_values))
print(dict1)
