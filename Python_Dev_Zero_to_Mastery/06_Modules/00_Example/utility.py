def print_name():
    print("Helloo")

def multiply(num1, num2):
    return num1 * num2

def divide(numer, denom):
    while True:
        try:
            return numer / denom 
        except (ValueError, ZeroDivisionError):
            print("Please enter a number that isn't 0")
        else:
            break