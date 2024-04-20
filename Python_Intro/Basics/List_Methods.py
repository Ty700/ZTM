basket = [1,2,3,4,5]

#Adding
new_list = basket.insert(1,100)

print(basket)
print(new_list)

# Notice how new_list is nothing... basket.insert doesn't get assigned to new_list
# Instead, all it does it insert 100 in the 1st index

# Extending
# Extend takes an iteratorable (? Spelling)
new_list = basket.extend([55])

print(basket)

# Removing
# Use pop
basket.pop()

print(basket)

# What about pop(0)

basket.pop(0)
# This remove the 0th index
print(basket)