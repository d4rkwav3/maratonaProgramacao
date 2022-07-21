'''
2.4.1.7 Lab – timestamping logger

Scenario

    Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
    Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
    Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

# import module responsible for time processing
from datetime import datetime

# get current time using now() method
timestamp = datetime.now()

# convert timestamp to human-readable string, following passed pattern:
string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

print(string_timestamp)


'''
from datetime import datetime as dt

def show_time(function):
    def wrapper(*args, **kwargs):
        time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
        print('{} performed at {}'.format(function.__name__, time))
        func =function(*args, **kwargs)
        return func
    return wrapper

@show_time
def soma (*args):
    somatorio = 0
    for i in args:
        if type(i) == int or type(i) == float:
            somatorio += i
        else:
            continue

    print(somatorio)

soma(1, 2, 3)