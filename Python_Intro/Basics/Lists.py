# Lists are a form of arrays

# Lists are mutable

# Example:

cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes',
]

#Will print all the members in the list
print(cart) 

# We can do:

cart[0] = 'laptop'

print(cart)

# Will print 2nd and 3rd index members
print(cart[1:3]) 

# Slicing a list does not alter the list, rather just a copy
# 28 proves 26 theory
print(cart)

# If we do:

new_cart = cart

#and then alter new_cart, it also affects the original cart

# Always have to specify what indexes I want to copy, even the whole list -> [:]
# Example, altering the new_cart will alter the original cart... I know it's dumb

new_cart[0] = 'something else'

print(new_cart)
print(cart)

#This will make a new cart in memory and altering it will not alter the original
new_cart_cart = cart[:]

new_cart_cart[0] = 'something else x2'

print(new_cart_cart)
print(cart)
