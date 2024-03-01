import time

def timestamp_from_ticks(ticks):
    
    milliseconds   = ticks / 10000
    milliseconds_r = int(milliseconds % 1000)
    seconds        = milliseconds / 1000
    seconds_r      = int(seconds % 60)
    minutes        = seconds / 60
    minutes_r      = int(minutes % 60)
    hours          = int(minutes / 60)

    # Format the time string
    time_format = f"{hours:02}:{minutes_r:02}:{seconds_r:02},{milliseconds_r:02}"

    return time_format