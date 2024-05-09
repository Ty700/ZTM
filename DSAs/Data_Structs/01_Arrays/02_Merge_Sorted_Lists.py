# Given two sorted arrays, return a merged array

def merge_sorted_arrays(list1, list2):
    # Create a new empty list

    # Two left pointers starting at index 0

    # value left ptr in list1 < list2 left ptr
        # if so:
            # append list1 left ptr to the list
            # inc list1 left ptr by 1
        
        # else not
            # append list2 left ptr to the list
            # inc list2 left ptr by 1

    # O(n + m) -> n = size of list1 and m = size of list2

    res_list = []

    curr_l1_index, curr_l2_index = 0, 0
    
    while(curr_l1_index != len(list1) or curr_l2_index != len(list2)):

        if(curr_l1_index == len(list1)):
            res_list.append(list2[curr_l2_index])
            curr_l2_index += 1
        
        elif(curr_l2_index == len(list2)):
            res_list.append(list1[curr_l1_index])
            curr_l1_index += 1
        
        elif(list1[curr_l1_index] < list2[curr_l2_index]):
            res_list.append(list1[curr_l1_index])
            curr_l1_index += 1
        else:
            res_list.append(list2[curr_l2_index])
            curr_l2_index += 1

    return res_list

print(merge_sorted_arrays([0,3,4,31,32,45,100], [4,6,30]))