class User:
    def sign_in(self):
        print("Logged in")
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print(f"Attacking with {self.power}!")
    
    def check_power(self):
        print(f"{self.name}\'s power: {self.power}")

class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        self.num_of_arrows -= 1
        print(f"{self.name} attacked and lost an arrow.")
        print(f"Number of attacks left: {self.num_of_arrows}")

    def check_arrows(self):
        print(f'{self.name}\'s arrows: {self.num_of_arrows}')

    def run(self):
        print("Ran really fast")
# What if we want to make another class that is a hybrid of Archer and Wizard?

class HybridBorg(Wizard, Archer): # Can give it as many other classes to inherit from
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

new_player = HybridBorg(name = "Borger", power = 50, arrows = 100)
new_player.run()

# This will error because we don't give the amount of arrows
# We have to run the init of each inherited class and specify what the init takes
# Also, helps if you name the variables when creating the object
new_player.check_arrows()
new_player.check_power()