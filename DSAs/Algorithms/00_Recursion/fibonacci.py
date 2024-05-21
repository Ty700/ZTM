def fib_seq(number):
    if number < 0:
        print('Error: Negative Number')
        return
    
    if number < 2:
        return number
    else:
        return fib_seq(number-1) + fib_seq(number-2)

# nth index 0 = 0, 1 = 1, 2 = 1, 3 = 2, 4 = 5....
print(fib_seq(9))