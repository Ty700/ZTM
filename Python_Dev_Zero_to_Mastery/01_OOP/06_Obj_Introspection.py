# Obj Introspection = finding the type of an obj at run time
class User():
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print("Logged in")
    

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) 
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"Attacking with power of {self.power}")

wizard1 = Wizard("Merlin", 60, 'merlin@gmail.com')

# Object Introspection:
print(dir(wizard1))