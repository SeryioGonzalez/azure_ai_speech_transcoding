import time

def time_from_ticks(ticks) -> time :
    
    microseconds_1 = ticks / 10
    microseconds_2 = microseconds_1 % 1000000
    seconds_1 = microseconds_1 / 1000000
    seconds_2 = seconds_1 % 60
    minutes_1 = seconds_1 / 60
    minutes_2 = minutes_1 % 60
    hours = minutes_1 / 60
    print(hours)
    time_result = time(int(hours), int(minutes_2), int(seconds_2), int(microseconds_2))

    print(time_result)

    return time_result