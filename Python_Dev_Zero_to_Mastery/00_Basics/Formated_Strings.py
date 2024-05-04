# What if we wanted a dynamic string

name = "Johnny"
age = 21
print("hi" + name)

# This can work but we'd have to add a + for every var

# Also each var has to be a string, rather just use print(f"")
# Example:

print(f"Hello {name}")

#or

print("Hello {}. You are {} years old"
    .format(name, age))

# or

birth_year = input("When were you born? ")

age = 2024 - int(birth_year)

print(f"You are {age} years old.")
