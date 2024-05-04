# Create a cat obj with a name and age member
# Create a function that finds the oldest cat
# Print out: "The oldest cat is X years old." <= X is the age of the oldest cat returned by the function above

class Cat:
    def __init__(self, name,age):
        self.name = name
        self.age = age

# Create a function that finds the oldest cat
def find_oldest_cat(list_of_cats):
    oldest_cat = max(list_of_cats, key = lambda x: x.age)
    return oldest_cat

# Create cat obj
tobi = Cat('tobi', 12)
molly = Cat("molly", 10)
megatron = Cat("megatron", 4)

cat_list = [tobi, molly, megatron]

# Print out: "The oldest cat is X years old." <= X is the age of the oldest cat returned by the function above
print(f"The oldest cat is {find_oldest_cat(cat_list).age} years old.")