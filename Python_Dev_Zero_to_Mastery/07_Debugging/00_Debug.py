# 1. Linting
    # Allows us to detect issues with code
    # Example
# num + 4 # pyflakes linter finds error without compiling code

# pylint is a package for linting

# 2. Use an IDE
    # Auto-formating
    # Detect errors in code with highlighting

# 3. Learn to read errors

# He didn't really go over much I didn't already know

# pdb -> gdb but for python. Have to import it

import pdb

def add(num1, num2):
    pdb.set_trace() # will pause here, like a breakpoint
    return num1 + num2

add(4, 'asdasdad')

# pdb commands:
# help -> Prnits help menu

# help list -> Prints help for list

# step, stepover, continue, etc