# Functions that start with two underscores are "dunder" methods
# Functions like len() are made from dunder methods

# Example:

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    # def __del__(self):
    #     print("Deleted!")

    def __call__(self):
        return 'yes??'

    # This will return a value in a dictionary
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy("red", 0)

# These two are the same
print(action_figure.__str__())
print(str(action_figure))

# However, we can customize what __str__ does, back to the class now

# Now we see that __str__ or str() returns "red"
# However, if we use str on anything that isn't an object of type Toy, we get the default str/__str__ function

print(len(action_figure))
print(len("HELLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOOoo"))

# Typically del removes deletes a variable in our program
# del action_figure

print(action_figure()) # With __call__ we can call an object, however, we have to comment out del since it deletes the obj

print(action_figure['name']) #Uses the __getitem__ dunder