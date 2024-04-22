# Zip: takes two iterables and combines them
# puts the first element of each list and makes a tuple of them
# puts the seconds element of each list and makes a tuple of htem
# goes for each iterable

# What happens if one list len is greater than the other? 
    # It will only zip up until the len of the smaller list

# Zip can take more than two iterables as well

# Can take a tuple, list, etc, anything that can be iterated over

# Creates a whole new iterable

my_list = [1,2,3,4,5]
your_list = [10,20,30]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return (item % 2 != 0)

another_list = list(zip(my_list, your_list))
print(another_list)