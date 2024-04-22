def add(num1, num2):
    try:
        return num1 + num2
    # except TypeError as err:    # If program catches TypeError, put it as err variable
                                # We can then print out err to show what the error was 
        # print("Something went wrong")

    # We can also wrap errors together like:
    except (TypeError, ZeroDivisionError):
        print("Oops")
    
print(add('1', 2)) # TypeError