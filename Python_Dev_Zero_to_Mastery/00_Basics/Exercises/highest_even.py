# Make a function that will print the highest even number from 
# an unsorted list of ints

def highest_even(arr):
    ret = 0

    for num in arr:
        if (num % 2 == 0) and (num > ret):
            ret = num

    return ret

make_list = [1,4,18,2,8,12,16]
print(highest_even(make_list))