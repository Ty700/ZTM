from functools import reduce

# Functools is a "toolbelt" and reduce is the specific tool

my_list = [1,2,3]

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return (item % 2 == 0)

# When reduce calls this function
# It will pass the first 0th index
# Then acc is the base value to add to
def accumulator(acc, item):
    # print(acc, item) # (0,1) then (1,2) then (3,3), then 6
    # It essentially reduces the list down to a single value
    # It starts a value defined by the 3rd parameter passed
    return acc + item
    
print(reduce(accumulator, my_list, 0))