class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def traverse(self, curr_node=None) -> None:
        if curr_node is None:
            curr_node = self.root
        
        if curr_node is None:
            return
        
        if curr_node.left:
            self.traverse(curr_node.left)
        
        if curr_node.right:
            self.traverse(curr_node.right)

        print(f'{curr_node.val}')

    def insert(self, val):
        new_node = Node(val)
        
        if not self.root:
            self.root = new_node
            return
        
        trav = self.root
        
        while True:
            if new_node.val < trav.val:
                if trav.left is None:
                    trav.left = new_node
                    break
                else:
                    trav = trav.left
            else:
                if trav.right is None:
                    trav.right = new_node
                    break
                else:
                    trav = trav.right
    
    def lookup(self, val_to_find, curr_node = None):
        if not curr_node:
            curr_node = self.root

        print(f'{curr_node.val}')

        if curr_node.val == val_to_find:
            return curr_node
        
        if val_to_find < curr_node.val:
            if curr_node.left:
                return self.lookup(val_to_find, curr_node.left)
            else:
                return None
        else:
            if curr_node.right:
                return self.lookup(val_to_find, curr_node.right)
            else:
                return None

    def remove(self, val_to_delete, curr_node = None):
        if not curr_node:
            curr_node = self.root
        
        parent_node = None

        while curr_node:
            if val_to_delete < curr_node.val:
                parent_node = curr_node
                curr_node = curr_node.left
            
            elif val_to_delete > curr_node.val:
                parent_node = curr_node
                curr_node = curr_node.right

            elif val_to_delete == curr_node.val:
                if not curr_node.right:
                    if not parent_node:
                        self.root = curr_node.left
                    else:
                        if curr_node.val < parent_node.val:
                            parent_node.left = curr_node.left
                        else:
                            parent_node.right = curr_node.left            
                
                elif not curr_node.right.left:
                    if not parent_node:
                        self.root = curr_node.left
                    else:
                        curr_node.right.left = curr_node.left

                        if curr_node.val < parent_node.val:
                            parent_node.left = curr_node.right
                        else:
                            parent_node.right = curr_node.right
                
                else:
                    pass 


def main() -> None:
    # Create the tree and insert the values
    my_bst = BinarySearchTree()
    my_bst.insert(9)
    my_bst.insert(4)
    my_bst.insert(6)
    my_bst.insert(20)
    my_bst.insert(1)
    my_bst.insert(15)
    my_bst.insert(170)

    # Traverse the tree
    my_bst.traverse()

    num_to_find = 21
    print('Trying to find: %d' % num_to_find)
    node_found = my_bst.lookup(num_to_find)

    if node_found and node_found.val == num_to_find:
        print('Found the node!')
    else:
        print('Couldn\'t find node')

if __name__ == '__main__':
    main()