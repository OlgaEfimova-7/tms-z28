import argparse
import csv
from datetime import timedelta
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-ta', '--task', required=True)
parser.add_argument('-t', '--time-to-focus-in-minutes', default=25, type=int)
parser.add_argument('-b', '--break-in-minutes', default=5, type=int)
parser.add_argument('-l', '--loops', default=4, type=int)
args = parser.parse_args()

with open('task_14_2_log_file.csv', 'a') as my_file:
    csv_writer = csv.writer(my_file)
    row = [args.first_name, args.last_name, args.time_to_focus_in_minutes, args.break_in_minutes, args.loops, args.task]
    csv_writer.writerow(row)


def generation(time_to_focus, breaktime, loops):
    seconds_to_focus = time_to_focus * 60
    seconds_to_relax = breaktime * 60
    while loops > 0:
        yield str(timedelta(seconds=seconds_to_focus))
        seconds_to_focus -= 1
        sleep(1)
        if seconds_to_focus == 0:
            print('BREAK!!!!')
            while True:
                yield str(timedelta(seconds=seconds_to_relax))
                seconds_to_relax -= 1
                sleep(1)
                if seconds_to_relax == 0:
                    print('THE END OF BREAK!')
                    break
            loops -= 1
            seconds_to_focus = time_to_focus * 60
            seconds_to_relax = breaktime * 60


generator = generation(args.time_to_focus_in_minutes, args.break_in_minutes, args.loops)
for i in generator:
    print(i)
