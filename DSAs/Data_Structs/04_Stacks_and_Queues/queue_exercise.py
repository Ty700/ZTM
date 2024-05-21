class Node():
    def __init__(self, val) -> None:
        self.data = val
        self.next = None

class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
    
    def peek(self):
        try:
            print(self.first.data)
        except (TypeError, AttributeError) as err:
            print('Queue is empty')
    
    def enqueue(self, val):
        new_node = Node(val)

        if not self.last and not self.first:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    
    def dequeue(self):
        try:
            data_to_ret = self.first.data
            node_to_del = self.first
            self.first = self.first.next
            del node_to_del
            return data_to_ret
        except (TypeError, AttributeError):
            print('Queue is empty')

my_q = Queue()

my_q.dequeue()
my_q.peek()
my_q.enqueue('Google.com')
my_q.peek()
my_q.enqueue('ZTM.com')
my_q.peek()
my_q.enqueue('Discord')
my_q.peek()
print(f'Deleting {my_q.dequeue()}')
my_q.peek()
print(f'Deleting {my_q.dequeue()}')
my_q.peek()
print(f'Deleting {my_q.dequeue()}')
my_q.peek()