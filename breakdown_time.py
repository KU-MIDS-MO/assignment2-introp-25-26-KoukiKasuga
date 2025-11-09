def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    
    hour = seconds//3600
    minute = (seconds - hour*3600)//60
    seconds_out = seconds - hour *3600 - minute*60

    broken_down_time = {3600: hour, 60: minute, 1: seconds_out}
    if hour == 0:
        broken_down_time.pop(3600)
    if minute == 0:
        broken_down_time.pop(60)
    if seconds_out == 0:
        broken_down_time.pop(1)
    return broken_down_time
    pass