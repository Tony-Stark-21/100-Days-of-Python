import time

current_time = float(time.time())
print(current_time)  # seconds since Jan 1st, 1970


# # Write your code below 👇

def speed_calc_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function()
        end_time = time.time()
        difference = end_time - start_time
        print(f"{function.__name__} run speed: {difference} s")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()