# A Higher Order Function can be one of two things:
    #1 A function that accepts another function
    #2 A function that returns another function

#1 Example:
def greet(func):
    func()
    
#2 Example:
def greet2():
    def func():
        return 5    
    return func

# Another example:

    # map, filter, reduce, etc are all higher order functions

