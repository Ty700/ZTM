# Decorators
def hello():
    print('Hello')

def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_function

@my_decorator
def hello(greeting, greeting2 = ':)'):
    print(greeting, greeting2)

hello("Hi")

# Why the hell would you do this? Well, we can do anything inside the wrap_function
# So maybe we do it for debugging? To see exactly where the debug statements are?? idk
# To call a decorator, we do @dec_name and then we def the function we want to be send to the decorator right under it

# What happens if hello took a parameter?

# A decorator is a higher order function that wraps another function?

# What happens if there are two parameters passed?

# Well we have to add a new parameter each time in the decorator, instead we use:
# def my_decorator(*args, **kwargs)

# This is a common pattern in python

# *args, **kwards is the "Decorator Pattern"