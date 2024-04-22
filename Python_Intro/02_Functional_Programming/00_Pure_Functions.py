# What is a pure function?
# We have a box that is a function. 
# We give this box a list, what we expect from a pure function, to give an output
# 2 Rules:
    # Give the same input, will always return the same output
    # Function should not produce any side effects
        # What are side effects?
            # Side Effects: Are things that affect the outside scope
                # I.e Printing something inside a function

# Example:

def multiply_by2(li):
    new_list = []
    for num in li:
        new_list.append(num * 2)
    return new_list

print(multiply_by2([1,2,3,4,5]))

# Is this a pure function?
    # Well does it pass rule 1? It gives the same output each time - so yes
    # Rule 2? It doesn't affect anything in the outside world, so yes
        # However, what if we had print inside the function? Then it wouldn't be pure.
        # Also, what happens if we declared new_list above the function? Then it wouldn't be pure since it's affecting
        # a non-local variable
    
# However, having all pure functions in a program is impossible. If a function doesn't affect the outside world, then 
# we wouldn't have programming