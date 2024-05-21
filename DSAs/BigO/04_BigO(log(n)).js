/*

Figuring out the amount of nodes on a level:
    Note: Levels start with 1
    2^(level - 1)

Level 0: 2^0 = 1 Node
Level 1: 2^1 = 2 Nodes
Level 2: 2^2 = 4 nodes
Level 3: 2^3 = 8 nodes
...
...
...
Level n: 2^n nodes

Figuring out the height or how many levels there are in a tree:

log(# of nodes) = height

The max amount of decisions to make to get to the end of the tree = log(amount of nodes)
*/