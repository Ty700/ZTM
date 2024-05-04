# from utility import print_name # This specifically only imports the one function
# from utility import * # This imports the whole library
import utility # Thsi imports the whole library as well, but we have to do utility.func_name()


# Everytime we import stuff, a __pycache__ folder is created
# .pyc = c python interpreter
# Essentially the __pycache__ will store theh compiled version of the imported module
# This compilation runs once (if no alterations are made to the file) so it saves time if we have to run the program again

utility.print_name() # It can only see print_name because we imported it

print(utility.multiply(100,2))
print(utility.divide(100,10))
