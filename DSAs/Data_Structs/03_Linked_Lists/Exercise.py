# Create a linked list where 10 -> 5 -> 16

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# node1 = Node(10)
# node2 = Node(5)
# node1.next = node2
# node3 = Node(16)
# node2.next = node3

# trav = node1

# while(trav != None):
#     print(trav.data)
#     trav = trav.next

#--------------------------------------------------------------------------------------------------------------#

# Now add a function where it appends a node to the linked list

# def append_to_list(head, node):
#     while(head.next != None):
#         head = head.next
#     head.next = node

# node1 = Node(10)
# head = node1
# node2 = Node(5)
# node3 = Node(16)

# append_to_list(head, node2)
# append_to_list(head, node3)

# trav = head
# while trav != None:
#     print(trav.data)
#     trav = trav.next

#--------------------------------------------------------------------------------------------------------------#

# Now add a function where it prepends a node to the linked list
# This would get too long, so I implemented insert and remove in this example as well

# Prepend:
# 100 -> 10 -> 5 -> 16 
# Add 100 to the beginning

# Insert - Given an index
# insert(2, 20)
#   100 -> 5 -> 20 -> 16

# Remove - Given an index
# remove(1)
#   100 -> 20 -> 16 

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.length += 1
            return None
        
        current = self.head
        
        while current.next != None:
            current = current.next

        current.next = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index < 0 or index > self.length:
            print('Index Error')
            return None
        
        if index == 0:
            self.prepend(data)
            return None
        
        if index == self.length:
            self.append(data)
            return None
        
        trav = self.head
        node_to_insert = Node(data)

        for _ in range(index - 1):
            if trav == None:
                print('Index out of range')
                
            trav = trav.next

        node_to_insert.next = trav.next
        trav.next = node_to_insert
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            print('Index Error')
            return None

        trav = self.head
        for _ in range(index - 1):
            trav = trav.next
        
        print('Removing: %d' % trav.next.data)

        if not trav.next.next:
            trav.next = None
        else:
            trav.next = trav.next.next

        self.length -= 1
    
    def reverse(self):
        trav = self.head
        prev_node = None

        while trav:
            next_node = trav.next
            trav.next = prev_node

            prev_node = trav
            trav = next_node
        
        self.head = prev_node

    def print_list(self):
        trav = self.head
        while(trav != None):
            print(trav.data)
            trav = trav.next

my_list = LinkedList()

my_list.append(10)
my_list.append(5)
my_list.append(16)
my_list.prepend(100)
my_list.insert(2, 20)
my_list.insert(0, 5000)
my_list.insert(my_list.length, 100000000000)
my_list.insert(-1, 0)
my_list.append(777)
my_list.print_list()
print("Reverse")
my_list.reverse()
my_list.print_list()