# List/Set/Dict Comprehensions

# Able to use comprehensions with list, sets, or dicts

# A quick way to create lists, sets, or dicts
# Instead of looping or appending

# Instead of doing:

my_list = []

# The 'C' way of doing things
for char in 'hello':
    my_list.append(char)

print(my_list)

# Rather do this:

# my_list = [param for param in iterable]

my_list = [character for character in "Helllllllllo"]

print(my_list)

my_list2 = [number for number in range(101)]

print(my_list2)

# what if we wanted all the numbers squeared?
# We can expand on this:
# Essentially treat the first param as an expression
my_list3 = [number**2 for number in range(101)]
print(my_list3)

# What if we want to only keep the even numbers?
# we can add an if statement at the end
# This is honestly stupid and cumbersome to read
# It's like the worst way to do things if you wanted to write clean code imo
my_list4 = [number**2 for number in range(101) if number % 2 == 0]
print(my_list4)

# Set Comprehension
# Essentially the same for a list, but with {}

my_list5 = {character for character in "Helllllllllo"}
print(my_list5)

my_list6 = {number for number in range(101)}
print(my_list6)

my_list7 = {number**2 for number in range(101)}
print(my_list7)

my_list8 = {number**2 for number in range(101) if number % 2 == 0}
print(my_list8)

# Dict Comprehension

simple_dict = {
    'a': 1,
    'b': 2,
}

# Goes through each dictionary item and alters them by the expression in the beginning
my_dict1 = {key + str(1): value**2 for key,value in simple_dict.items()}
my_dict2 = {key + str(1): value**2 for key,value in simple_dict.items() if (value % 2 == 0)}

print(my_dict1)
print(my_dict2)

# Can we pass a list and make a dictionary with the list being the key and alteration being a value?
my_dict3 = {num: num*2 for num in [1,2,3]}
print(my_dict3)