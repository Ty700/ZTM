def collectDriverAge():
    age = int(input("What is your age?: "))
    return age

def checkDriverAge():
    age = collectDriverAge()

    if (age > 18):
        print("Powering on. Enjoy the ride!")
    elif age == 18:
        print("Enjoy your first ride!")
    else:
        print("You are too young to drive.")

checkDriverAge()