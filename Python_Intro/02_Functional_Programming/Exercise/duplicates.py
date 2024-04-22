# Using what we know about list comprehensions, make a list without duplicates

original_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

new_list = set([character for character in original_list if original_list.count(character) > 1])

print(list(new_list))

