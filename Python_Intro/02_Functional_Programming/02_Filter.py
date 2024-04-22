# Want to create a function that checks if a number is odd and only return them
# Filter: If the item in an iterable is true, it will keep it. If not, it will get ride of it

my_list = [1,2,3,4,5,6,7,8,9,10]

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return (item % 2 != 0)

# Filters out the odds
my_list = filter(only_odd, my_list)

# Say we want to take all the odds and multiply them by 2
my_list = map(multiply_by2, my_list)

# See how easy this is???
print(list(my_list))