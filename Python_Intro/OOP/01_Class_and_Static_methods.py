class PlayerCharacter:
    # Can we do something like we did for membership with methods?
    #   Yes, using decorators <- More on that later
    membership = True

    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
    
    def shout(self):
        print(f'My name is {self.name}!')

    # What does this do? Well, cls is the standard for class methods. 
    # How does this make this a class method? We can use it without instantiating a class

    @classmethod
    def adding_things(cls, num1, num2):
        # return num1 + num2
        return cls("teddy", num1 + num2)

    # What does this do? We use it when we don't care about any of the attributes
    # Won't see this very often
    @staticmethod
    def subbing_things(num1, num2):
        return num1 - num2

# See, we don't have a PlayerCharacter but can still call that method
print(PlayerCharacter.adding_things(1, 2)) # Will print out the mem loc on new obj

# Why would we do this? Well, in class methods we can init objs in them
new_player = PlayerCharacter.adding_things(2,3)
print(new_player.age)