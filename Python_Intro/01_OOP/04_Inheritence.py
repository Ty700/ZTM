# We have Users that can be Wizards, Archers, etc, but all of them have to be signed in

class User:
    # Where is init? Well, we only need init if we want to assign member to the class
    def sign_in(self):
        print("Logged in")
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print(f"Attacking with {self.power}!")

class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        self.num_of_arrows -= 1
        print(f"{self.name} attacked and lost an arrow.")
        print(f"Number of attacks left: {self.num_of_arrows}")

def player_attack(character):
    character.attack()

player1 = Wizard("Merlin", "Sparks")
player2 = Archer("Robin", 100)

player_attack(player1) # Polymorphism Example
player_attack(player2) # Attack() has a different result for each player since each player is a different class

# checking is something is an instance of a class
wizard1 = Wizard('Merlin', 'fire')
print(isinstance(wizard1, Wizard))   # Yes, wizard1 is an obj created from the Wizard class
print(isinstance(wizard1, User))     # Also yes, b/c Wizard is created from the User class
print(isinstance(wizard1, object))   # the object class is the root parent for all objs in python
                                    # This is where we get all the dunder methods
player_attack(wizard1)

# What if I had a method in the parent class I wanted to call but my obj class also had the same method name?
# Example:
class Person():
    def speak():
        print("Hello World!")

class Tyler(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # What if I wanted Tyler class to be able to call Person's speak? 
    def speak(self):
        # We can do: 
        Person.speak() # Look at 05_Super.py for a better way
        print(f"Hello, I am {self.name}")

me = Tyler("Tyler", 23)
me.speak()