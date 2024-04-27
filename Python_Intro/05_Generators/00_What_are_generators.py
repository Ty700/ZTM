# A list is stored in memory... 

my_list = [1,2,3,4,5]

# However, a generator creates a sequence of values but doesn't store them in memory

# Example:

range(100) # -> Where is range storing 0-99? Nowhere, it's just being make and then immediately deleted

# Anything that is a generator, is iterable
# Not everything that is iterable is a generator

# A list is an iterable, but not a generator

# A generator is a subset of an iterable

# The difference? How we implement them

# Generator functions typically prefaced with generator_
def generator_function(num):
    for i in range(num):
        yield i # What is yield? It will pause the function, give i back, then wait until a new function call to keep goin

for item in generator_function(50): # So this will give 0, generator_function will yeild 0 back, then it will print
    print(item)                     # Then since print is the last thing we do with the item, we went back to the function
                                    # It yieled 1, we printed it, went back, it yieled 2, so on and so forth

g = generator_function(50)

print(g)    # What is gonna happen? We can a generator object
next(g)     # This will be the first generated obj, so 0
next(g)     # This will be the second
next(g)     # Third
# ...       # It's like stepping through a for loop and using specific values at certain times. That's kinda cool ig

            # What happens if we have more nexts than the range?
            # We get an error, kinda like going outside the range of an array
            # Once we exceed the number of items in the list, it will error