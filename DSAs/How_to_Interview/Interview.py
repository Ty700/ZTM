# Given 2 arrays, create a function that let's a user know (T/F) whether these two arrays contain any common items

# For Example:


#{
#   'z': 0, 
#   'y': 1,
#   
#}

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
    # This would return False  

# array1 = ['a', 'b', 'c', 'x']
array3 = ['z', 'y', 'x']
    # Returns true

array4 = []

def find_pair(list, list2):
    pair_map = {}
    
    for index, value in enumerate(list):
        pair_map[value] = index

    for value in list2:
        if value in pair_map.keys():
            return True
        
    # If we wanted to return the indicies
        # for index, value in enumberate(list2):
            # if value in pair_map.keys():
                # return [index, pair_map[value]]

    return False

print(find_pair(array1, array2))

print(find_pair(array1, array3))

print(find_pair(array1, array4))