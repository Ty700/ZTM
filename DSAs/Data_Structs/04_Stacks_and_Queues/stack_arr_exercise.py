
class Stack():
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        try:
            val = self.stack.pop()
            return val
        except IndexError:
            print('Stack is empty')
    def peak(self):
        try:
            print(self.stack[len(self.stack) - 1])
        except IndexError:
            print('Stack is empty')
my_stack = Stack()

my_stack.push('Google.com')
my_stack.peak()
my_stack.push('ZTM.com')
my_stack.peak()
my_stack.push('Discord.com')
my_stack.peak()
my_stack.pop()
my_stack.peak()
my_stack.pop()
my_stack.peak()
my_stack.pop()
my_stack.pop()
my_stack.pop()