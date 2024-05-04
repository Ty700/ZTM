# MRO - Method Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C): # What is the value of num here??? My guess is 10 since B inherts from A first
    pass

print(D.num) # We actually get 1, since it the "closest" num to D is from C

# Kinda like which num is closest to D in scope
# We can check mro by:
print(D.mro())

#     Inheritence Tree:
#
#         object
#           |
#           A
#          / \
#         /   \
#        B     C
#         \   /
#          \ /
#           D

# MRO uses depth first search