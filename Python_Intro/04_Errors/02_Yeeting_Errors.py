while True:
    try:
        age = int(input("Enter a number: "))
    
    except ValueError:
        print("Please enter a number: ")
    
    except ZeroDivisionError:
        print("Please enter a number greater than 0")

    else:
        print("Thanks")
        break
    
    # This will run even after we have broken out of the loop... why?
    # This will run regardless at the end of everything, errors, no errors, etc
    # Why is this useful? Say we have someone trying to run into our server
    # We want to log that regardless of what happens
    finally:
        print("Okay, I am finally done")