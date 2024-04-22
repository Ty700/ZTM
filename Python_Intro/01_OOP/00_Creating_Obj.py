class BigObject: # Camel Case 
    pass

obj1 = BigObject()  # Notice the syntax is the same as creating anything, a list for example
                    # Thus a list is an obj, just like everything else in Py

my_list = []        # my_list is a list obj, obj1 is my own obj

# print(type(obj1))

# Say we have a game we want to make:

class PlayerCharacter: 
    # Class Object Attribute <= Not dynamic. Like a default value for all the objs that are create from this bp
    membership = True 
    hp = 50

    def __init__(self, name, age):   # Everytime you create an obj of type PlayerCharacter
        self.name = name        # def __init__ will run
        self.age = age          # self.<var_name> creates a variable for the obj

    def run(self):
        print(f"{self.name} is running!")
    

new_player = PlayerCharacter("Tyler", 23)

print(new_player.hp)

new_player.run()

print(f"{new_player.name}'s age is {new_player.age}!")
