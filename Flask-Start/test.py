import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(function):
    def time_calc():
        yo = current_time - time.time()
        function()
        return yo
    return time_calc


def fast_function():
    for i in range(1000000):
        i * i


def slow_function():
    for i in range(10000000):
        i * i


