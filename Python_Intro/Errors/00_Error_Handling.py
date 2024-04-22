# When we write programs, it will error

# A good programmer will allow a python program to run even if there are errors.
# This is called error handling

# So, how do we handle errors?
# What happens if we give a str with this? We get an error
# age = int(input('Enter your age: '))
# print(age)

# Thus, we can do this instead:

try:
    age = int(input("Enter your age: "))
    print(age)
except:
    # Whatever happened in try errors, do something here
    # rather than exiting the program
    print("Please enter a number")
    # However, we'd have to put it in a while loop to run indef
    
# while(True):
#     try:
#         age = int(input("Enter your age: "))
#         print(age)
#         break
#     except:
#         print("Please enter a number")


# Now, how do we handle different error types?
while True:
    try:
        age = int(input("Enter your age: "))
        10 / age # When we enter 0, it errors...

    except ValueError:
        print("Please enter a number")
    
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    
    # What happens if we add another ValueError? <= Does nothing. It will go to the first one and then go back to the loop
    except ValueError:
        print("!")

    else:
        print("Thanks")
        break