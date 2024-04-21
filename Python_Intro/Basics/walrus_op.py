# :=

# Assigns values to variables as as part of a larger expression

a = 'hellooooooooooooooooo'

if (len(a) > 10):
    print(f"too long {len(a)} elements")

# Where does := come in? 

# Well, we are wasting time calculating the len of a twice.

# Instead, we would do:

if ((n :=len(a)) > 10): # Note: walrus op has low priorty, so wrap it in parent
    print(f"Too long {n} elements")


# Example 2:

while((n := len(a)) > 1):
    print(n)
    a = a[:-1]
