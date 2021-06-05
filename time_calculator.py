def add_time(start, duration, starting_day=None):
    days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    [start_time, start_period] = start.split()
    [start_hour, start_minute] = start_time.split(':')
    [duration_hours, duration_minutes] = duration.split(':')

    start_hour = int(start_hour) + 12 if start_period == 'PM' and int(start_hour) < 12 else int(start_hour)
    start_minute = int(start_minute)
    duration_days = int(duration_hours) // 24
    duration_hours = int(duration_hours) % 24
    duration_minutes = int(duration_minutes)

    result_day = duration_days
    result_is_AM = start_period == 'AM'
    result_hour = start_hour + duration_hours
    result_minute = start_minute + duration_minutes

    if result_minute >= 60 :
        while result_minute >= 60 :
            result_hour += 1
            result_minute -= 60

    if result_hour >= 24 :
        while result_hour >= 24 :
            result_day += 1
            result_hour -= 24
            result_is_AM = result_is_AM == False
    elif result_hour >= 12 :
        result_is_AM = False
        if result_hour > 12 :
            result_hour = result_hour % 12

    result_period = 'AM' if result_is_AM else 'PM'
    result_minute = str(result_minute) if result_minute >= 10 else '0' + str(result_minute)

    final_result_string = str(result_hour) + ':' + str(result_minute) + ' ' + result_period

    if starting_day :
        day_start = days.index(starting_day.lower())
        day_name = days[(day_start + result_day) % len(days)].capitalize()

        final_result_string += ', ' + day_name

    if result_day :
        if result_day > 1 :
            final_result_string += ' (' + str(result_day) + ' days later)'
        else :
            final_result_string += ' (next day)'

    return final_result_string