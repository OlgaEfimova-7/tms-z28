import csv
fields = ['Name', 'Surname', 'Age']
rows = [['Ivan', 'Ivanov', '14'],
        ['Peter', 'Petrov', '17'],
        ['Alex', 'Romanov', '27'],
        ['Viktor', 'Sidorov', '23'],
        ['Max', 'Socolov', '44']
        ]
with open('first_file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)


def dict_writing(low_value, high_value, value, dict):
    key = f'{low_value}-{high_value}'
    if low_value <= value <= high_value:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    elif key not in dict:
        dict[key] = 0


def dict_writing_without_limit_value(low_value, value, dict):
    key = f'{low_value}+'
    if low_value <= value:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    elif key not in dict:
        dict[key] = 0


with open('first_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    fields = next(csv_reader)
    index_of_col = fields.index('Age')
    dict_1 = {}
    for row in csv_reader:
        for index, el in enumerate(row):
            if index == index_of_col:
                convert_el_into_int = int(el)
                dict_writing(1, 12, convert_el_into_int, dict_1)
                dict_writing(13, 18, convert_el_into_int, dict_1)
                dict_writing(19, 25, convert_el_into_int, dict_1)
                dict_writing(26, 40, convert_el_into_int, dict_1)
                dict_writing_without_limit_value(40, convert_el_into_int, dict_1)
    with open('result_file.csv', 'w') as csv_file2:
        csv_writer = csv.writer(csv_file2)
        csv_writer.writerow(dict_1.keys())
        csv_writer.writerow(dict_1.values())
