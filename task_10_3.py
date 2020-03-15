import csv
import datetime
with open('result3_file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    field = ['Date']
    rows = [['2018-09-10'], ['2015-05-11'], ['2020-02-23']]
    csv_writer.writerow(field)
    csv_writer.writerows(rows)

with open('result3_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    field = next(csv_reader)
    list_of_strings = (list(el for row in csv_reader for el in row))
    list_of_dates = list(datetime.datetime.strptime(date, '%Y-%m-%d') for date in list_of_strings)
    print(min(list_of_dates))
