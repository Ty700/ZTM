# Unordered pair of unique elements
my_set = {1,2,3,4,5}

print(my_set)

my_set_dupe = {1, 1, 2, 2, 3, 4, 5, 5}

print(my_set_dupe)

my_set_dupe.add(100)
my_set_dupe.add(100)
my_set_dupe.add(3)


print(my_set_dupe)

# What if we are given a list and wnat to create a set from it?

my_list = list(my_set_dupe)

print(my_list)

print(set(my_list))

# We can not do: my_set_dupe[0] -> sets are not callable