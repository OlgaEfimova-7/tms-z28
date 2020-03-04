from datetime import datetime, date, time, timedelta
list_of_trains = [{'Number of the train': 1,
                   'Point of departure': 'Minsk',
                   'Departure time': '14 hours 30 minutes',
                   'Point of arrival': 'Vitebsk',
                   'Arrival time': '17 hours 00 minutes'},

                  {'Number of the train': 2,
                   'Point of departure': 'Brest',
                   'Departure time': '8 hours 30 minutes',
                   'Point of arrival': 'Vitebsk',
                   'Arrival time': '17 hours 00 minutes'},

                  {'Number of the train': 3,
                   'Point of departure': 'Grodno',
                   'Departure time': '11 hours 30 minutes',
                   'Point of arrival': 'Minsk',
                   'Arrival time': '15 hours 00 minutes'},
                  ]
list_of_train_numbers = []
for i in list_of_trains:
    list_of_arrival_time = (i['Arrival time']).split()
    list_of_departure_time = (i['Departure time']).split()
    time_of_arrival = datetime(2020, 3, 4, int(list_of_arrival_time[0]), int(list_of_arrival_time[2]))
    time_of_departure = datetime(2020, 3, 4, int(list_of_departure_time[0]), int(list_of_departure_time[2]))
    difference = time_of_arrival-time_of_departure
    if difference > timedelta(0, 7*60*60+20*60):
        print(i['Number of the train'])
