# Given an array = [2,5,1,2,3,5,1,2,4]
# Return the first repeated character

def first_recurring_num(ls):
    num_occur = {}
    count = 0
    for num in ls:
        if num in num_occur.keys():
            return num
        
        num_occur[num] = True

    return None
print(first_recurring_num([2,5,1,2,3,5,1,2,4]))

print(first_recurring_num([2,5,1,0,7,5,1,2,4]))

print(first_recurring_num([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,0,1]))

print(first_recurring_num([]))
