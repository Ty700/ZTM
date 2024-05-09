# Collection of numbers
    # Return a pair of numbers that add up to the target
    # Return the indices

# Ask questions
    # How are they stored?
    # Repeating elements
    # Can we repeat the same number?
    # Negatives? Integers?

target = 8
collection = [1, 2, 3, 9]   # No 
collection2 = [1, 2, 4, 4]  # 4, and 4

# I am gonna use a two pointers


def find_pair_sorted(list, target):
    left  = 0
    right = len(list) - 1

    while(left < right):
        if (list[left] + list[right] > target):
            right -= 1
        elif(list[left] + list[right] < target):
            left += 1
        elif(list[left] + list[right] == target):
            return [left, right]
        else:
            return None

print(find_pair_sorted(collection, target))
print(find_pair_sorted(collection2, target))


# Okay, now what if they are unsorted?
# Well, as I go through the list, have I seen the complement to the current number I am at, to equal the target

def find_pair_unsorted(list, target):
    comp_map = {}

    for index, val in enumerate(list):
        if target - val in comp_map.keys():
            return [comp_map[val], index]
        else:
            comp_map[val] = index
        
    return None


print(find_pair_unsorted(collection, target))
print(find_pair_unsorted(collection2, target))
