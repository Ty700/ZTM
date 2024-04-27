def fib(num):
    a = 0
    b = 1
    
    for i in range(num):
        yield a         # We are yielding here so it can print it in the for loop later
        temp = a        # Now that we have printed our a, we can do some alterations to print it out again
        a = b           # Also, since we are yielding it isn't actually storing it in memory, we are just generating it to then use it somewhere else
        b = temp + b    # Really powerful actually

for x in fib(100): # 20th fib number is really the 19th
    print(x)

