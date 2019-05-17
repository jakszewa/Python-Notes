# create function
# calculate seconds

def print_seconds_per_day():
    hours = 24
    minutes = hours * 60
    seconds = minutes * 60
    
    return seconds

print(print_seconds_per_day())

# convert days to seconds

def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return seconds

print(convert_days_to_seconds(7))

# convert days to milliseconds

def convert_days_to_milliseconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return seconds

millisec = convert_days_to_milliseconds(7) * 1000

print(millisec)





