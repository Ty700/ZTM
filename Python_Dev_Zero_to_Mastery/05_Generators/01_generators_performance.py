# Generators are supposed to be fast in performance

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        print("=========")
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Total time: {end_time - start_time}")
        print("=========")
        return result
    return wrapper

@performance
def long_time(num):
    for i in range(num):
        i * 5

@performance
def long_time2(num):
    for i in list(range(num)):
        i * 5

long_time(1000000000)   # 27 seconds -> This one is using the generator
long_time2(1000000000)  # Killed -> Idk time but must've been longer than 27s