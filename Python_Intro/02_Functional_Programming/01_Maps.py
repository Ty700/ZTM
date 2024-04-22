# map(func, iterable)
    # Take an action, and apply it to the data 
    # map(action, data)

# So for example:

def multiply_by2(item):
    return (item * 2)

# Map returns a new list so we can to assign it to something
new_list = map(multiply_by2, [1,2,3,4,5])
print(list(new_list))

# However, if I pass a variable containing a list, map doesn't alter it in-place

my_list = [1,2,3]

# This is essentially doing nothing as we are not saving the result anywhere
map(multiply_by2, my_list)

# still [1,2,3]
print(my_list)

# Thus, this is a good example of why map is a pure function.
# It always results in the same output given the same input
# It doesn't have any side effects to the outside world
