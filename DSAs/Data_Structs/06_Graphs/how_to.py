# Graphs are built on-top of other data structures

# Trees and linked lists

#           2--------0
#          / \
#         /   \
#        /     \
#       1-------3 

# Edge List
graph = [[0,2], [2,3], [2, 1], [1, 3]]
    # 0 connects to 2
    # 2 connects to 3
    # 2 connects to 1
    # 1 connects to 3

# Adjacent List

# Index = node
# Values = Node neighbors

# 0 only connects to 2
# 1 connects to 2, and 3
# 2 connectes to everything (0,1,3)
# 3 connectes to 1, and 2
adj_graph = [[2], [2,3], [0,1,3], [1,2]]

# Adjacent Matrix
# 0 represents no link, 1 represents a link
    # Note: 1 can be changed to the weight of the link
# Index of the array = node number
# Index of the inner array = node
adj_max_graph = [
    [0,0,1,0],  # 0 connects to only 2
    [0,0,1,1],  # 1 connects to 2 and 3
    [1,1,0,1],  # 2 connects to 0, 1, and 3
    [0,1,1,0]   # 3 connects to 1, and 2
]

# We can even do something like:
# Now the key is the node
# and the value is the links the key node has
adj_max_graph_2 = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,1],
    3: [0,1,1,0],
}