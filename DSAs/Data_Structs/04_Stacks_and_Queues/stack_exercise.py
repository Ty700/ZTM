# Stack

class Node():
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
        self.prev = None

class Stack():
    def __init__(self):
        self.length = 0
        self.top = None
        
    def pop(self):
        try:
            delete = self.top
            self.top = self.top.prev
            del delete
        except AttributeError:
            print('Stack is empty')

    def peak(self):
        try:
            print(self.top.data)
        except AttributeError as err:
            print(f'Stack is empty')

    def push(self, val):
        if not self.top:
            self.top = Node(val)
        else:
            new_top = Node(val)
            new_top.prev = self.top
            self.top.next = new_top
            self.top = new_top

my_stack = Stack()

my_stack.push('Google.com')
my_stack.push('ZTM.com')
my_stack.push('Discord.com')
my_stack.peak()
my_stack.pop()
my_stack.peak()
my_stack.pop()
my_stack.peak()