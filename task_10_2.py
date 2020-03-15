import csv
from functools import reduce
with open('result10_file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    fields = ['Data', 'Place', 'Degrees', 'Wind Speed']
    rows = [['07.03.2020', 'Minsk', '7', '3'],
            ['08.03.2020', 'Minsk', '9', '4'],
            ['09.03.2020', 'Minsk', '8', '3'],
            ['10.03.2020', 'Minsk', '9', '5'],
            ['11.03.2020', 'Minsk', '6', '8'],
            ['12.03.2020', 'Minsk', '9', '13'],
            ['13.03.2020', 'Minsk', '9', '12']
            ]
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)


def list_of_elements_of_column(number_of_col):
    result = [int(elem) for rows in csv_reader for i, elem in enumerate(rows) if i == (number_of_col - 1)]
    return result


with open('result10_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    list_of_degree = list_of_elements_of_column(3)
    average_degree = (reduce(lambda x, y: x + y, list_of_degree)) / len(list_of_degree)
    print(average_degree)

with open('result10_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    list_of_wind_speed = list_of_elements_of_column(4)
    average_speed = (reduce(lambda x, y: x + y, list_of_wind_speed)) / len(list_of_wind_speed)
    print(average_speed)
