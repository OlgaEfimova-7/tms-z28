import argparse
import csv
from datetime import timedelta
from datetime import datetime
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-ho', '--hours', required=True, type=int)
parser.add_argument('-m', '--minutes', required=True, type=int)
parser.add_argument('-s', '--seconds', required=True, type=int)
args = parser.parse_args()
with open('task_14_1_log_file.csv', 'a') as my_file:
    time_now = datetime.now()
    row = [args.first_name, args.last_name, f'{time_now.hour}:{time_now.minute}:{time_now.second}']
    csv_writer = csv.writer(my_file)
    csv_writer.writerow(row)


def iteration(hours, mins, secs):
    seconds = hours*3600 + mins*60 + secs
    seconds_now = time_now.hour * 3600 + time_now.minute * 60 + time_now.second
    delta_seconds = seconds - seconds_now
    while True:
        if delta_seconds < 0:
            print('This time has passed')
            break
        yield str(timedelta(seconds=delta_seconds))
        sleep(1)
        if delta_seconds == 0:
            print('ALARM!!!')
            break
        delta_seconds -= 1


generator = iteration(args.hours, args.minutes, args.seconds)
for i in generator:
    print(i)
