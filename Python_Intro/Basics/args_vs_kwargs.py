# args vs *args **kwargs

# def super_func(args):
#     return sum(args)

# Note: *args & **kwargs can be changed to anything
# def super_func(*args):
#     return sum(args)

def super_func(*args, **kwargs):
    print(kwargs)   # passed as dict  
    print(args)     # passed as list

    #with **kwargs, we need to go through each and sum them since they are passed as a dict
    total = 0
    for num in kwargs.values():
        total += num
    return sum(args) + total

# print(super_func(1,2,3,4,5)) #-> Will fail if *args is changed to args 

print(super_func(1,2,3,4,5, num1=5, num2=10))
