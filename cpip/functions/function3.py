# create function
# calculate seconds

def print_seconds_per_day():
    hours = 24
    minutes = hours * 60
    seconds = minutes * 60
    
    return seconds

print(print_seconds_per_day())

def print_seconds_per_day(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return seconds

print(print_seconds_per_day(7))