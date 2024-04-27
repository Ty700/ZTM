# What if we want to add an entire folder?

# A package is simply a folder we want to import
# A module is a file that might be within a package

# so how do we import shopping_cart from 01_Example?

import shopping.shopping_cart

cart = shopping.shopping_cart.buy('apple')

print(cart)