# A dictionary is a hash map - unordered key: value pair

# Dictionary keys need to be immutable -> can't change
# Keys also need to be unique

dictionary = {
    'a': 1,
    'b': 2,
}

# a is the key, 1 is the value

# Will search for the 'b' key and return its value
print(dictionary['b'])

# Dictionaires can have different key and pair types

dictionary_2 = {
    'a': [1,2,3],
     2: 'hello',
    'z': True
}

print(dictionary_2[2])
print(dictionary_2['z'])
print(dictionary_2['a'])


# We can have a list of dictionaries

my_list = [
    {
    'a': 1,
    'b': 2,
    }, 
    {
    'a': [1,2,3],
     2: 'hello',
    'z': True
    }   
]

print(my_list[0]['a'])      #1
print(my_list[1]['a'][2])   #3