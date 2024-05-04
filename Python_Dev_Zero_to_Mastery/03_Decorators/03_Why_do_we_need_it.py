# A common decorator is to time the time it takes to complete a function
from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        print('***********')
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'It took: {end_time - start_time} s')
        print('***********')
        return result  
    return wrapper

@performance
def long_time():
    for i in range(1000000000):
        i * 5

long_time()
