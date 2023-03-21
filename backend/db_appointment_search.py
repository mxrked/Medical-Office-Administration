from datetime import time, datetime, timedelta




taken_appointments_dict = {
    time(hour=9, minute=00) : timedelta(minutes=10),
    time(hour=9, minute=10) : timedelta(minutes=10),
    time(hour=9, minute=20) : timedelta(minutes=10),
    time(hour=9, minute=30) : timedelta(minutes=10),
    time(hour=9, minute=40) : timedelta(minutes=10),
    time(hour=9, minute=50) : timedelta(minutes=10),
    time(hour=10, minute=0) : timedelta(minutes=10),
    time(hour=10, minute=10) : timedelta(minutes=10)
}
taken_appointments_dict = {}


possible_appointment_times = []

appointment_length = timedelta(minutes=10)

start_search_time = time(hour=9, minute=0)
search_end_time = time(hour=17, minute=0)

last_possible_time = datetime.combine(datetime.today(), search_end_time)

possible_time = datetime.combine(datetime.today(), start_search_time)


"""
    Ok, this is the hard part.
    We use a pointer to loop through our starting time and end time.
    Think of possible_time as the time we are testing, like 10:00
"""
while possible_time < last_possible_time :

    # We loop through our list of taken appointment times
    for taken_appointment in list(taken_appointments_dict.keys()):
        # Converting appointment to datetime so we can compare using timedelta
        taken_appt_start_time = datetime.combine(datetime.today(), taken_appointment)
        # Our dictionary contains timedeltas as the appointment length
        taken_appt_end_time = taken_appt_start_time + taken_appointments_dict[taken_appointment]


        possible_endtime = possible_time + appointment_length

        # We first check if the possible starting time if it is inbe6tween our appointment
        # Then we check if the possible endtime is inbetween our appointment
        if ((possible_time >= taken_appt_start_time and possible_time < taken_appt_end_time) or
            (possible_endtime > taken_appt_start_time and possible_endtime < taken_appt_end_time)):
            # If its in between It means we can't use this time!
            # We must skip ahead to the end of this appointment to look for avaliable times!
            possible_time = taken_appt_end_time
            break

    else:
        # This activates if the for loop doesn't break, this means that it didn't interfer with our
        # taken appointments!
        possible_appointment_times.append(possible_time)
        # Now we must skip ahead to look for more times
        possible_time += appointment_length


possible_appointment_times = [dt.time() for dt in possible_appointment_times]

print(len(possible_appointment_times))
for every_time in possible_appointment_times:
    print(every_time)