from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

#3 Filter the scores that pass over 50%
scores = [73, 29, 65, 19, 76, 100, 88]

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). Whis the total?

#1 

def cap_name(name):
    return name.capitalize()

my_pets = map(cap_name, my_pets)

print(list(my_pets))

# 2
my_numbers.sort()
zipped_lists = zip(my_strings, my_numbers)
print(list(zipped_lists))

# 3

def filer_out_below_50(num):
    return (num > 50)

filter(filer_out_below_50, scores)

print(list(scores))

# # 4
def accumulate(acc, num):
    print(acc, num)
    return acc + num

final_result = reduce(accumulate, scores, 0)
final_result = reduce(accumulate, my_numbers, final_result)

print(final_result)