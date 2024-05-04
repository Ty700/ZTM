# There is a better way to call a method from a parent class 


class User():
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print("Logged in")
    

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email) # This is equivalent to line 14. Cleaner way of doing it. However, what if we have multiple inherits???
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"Attacking with power of {self.power}")

wizard1 = Wizard("Merlin", 60, 'merlin@gmail.com')
print(wizard1.email) # This will error if we don't have line 13