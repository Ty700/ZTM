# Useful built-in modules

# Specialized Data Types come from std lib of python
    # Not seen everywhere

# Collection module
from collections import Counter, defaultdict, OrderedDict

# Counter and OrderedDict are classes, defaultdict is a function
# Going to PyPi tells you more about collections

li = [1,2,3,4,5,6,7]

print(Counter(li)) # Creates a dict that keeps track of the times and element is in the list

sent = 'Blah blah blah thing about python'

print(Counter(sent)) # Creates a dict of each character in the sent and how many times it has been used

#defaultdict

dictionary = defaultdict(
    # Needs a callable object for when we search for a key that isn't in the dict, it will call the object
    lambda: -1,
    {
        'a': 1,
        'b': 2,
    }
)

print(dictionary['a']) # 1
print(dictionary['c']) # Error -> This is where defaultdict comes in

# OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2

d2 = OrderedDict()

d2['a'] = 1
d2['b'] = 2

print(d2 == d) # True

# If we change the order of insertion:


d3 = OrderedDict()

d3['b'] = 2
d3['a'] = 1


d4 = OrderedDict()

d4['a'] = 1
d4['b'] = 2

print(d4 == d3) # False, so an OrderedDict looks to see if the order of insertion is the same

# Date and Time module

import datetime

print(datetime.time())
                    
print(datetime.time(5,45,2)) #5H 45M 2S

print(datetime.date.today()) # Prints the day 

# Time module -> Used this for the performance decorator

import time

# Array packages

from array import array

# Lists in pythons are sometimes called arrays

# lists in python are dynamic, increment the array as needed, obv arrays can't
# arrays take less memory? Idk about that one, depends on how much you give it