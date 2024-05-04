# Decorators start with a @

# First to understand decorators, we need to understand functions

# Functions are first-class citizens
    # They can be passed as parameters
    # Treated as variables

def hello():
    print("helllllooooooooo")

greet = hello

# if I del hello

del hello

# It will delete the name of the function hello(), however, since greet still points to it.
# From there are on you can't do hello(), but greet() still works
# Thus, Python won't delete the function entirely if there is something pointing to it still
print(greet())

# So why is this important?
# Decorators is only possible because of these features

# Decorators supercharge our function 
# For example, if we add @ to a function, we can add extra functionality to it
