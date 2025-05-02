# Merge, unlike the elementary sorts, are O(nlogn)
# Elementary sorts were O(n^2)
# Merge and Quick sort uses the "Divide and Conquer" method

import time

def merge(left, right):
    sorted_li = []
    while left and right:
        if left[0] < right[0]:
            sorted_li.append(left[0])
            left.pop(0)
        else:
            sorted_li.append(right[0])
            right.pop(0)
        
    if len(left) > 0:
        sorted_li += left
    
    if len(right) > 0:
        sorted_li += right
    
    return sorted_li

def merge_sort(li):
    if len(li) <= 1:
        return li

    left = li[:(len(li))//2]
    right = li[len(li)//2:]

    return merge(
        merge_sort(left),
        merge_sort(right)
    )

def main():
    li = [x for x in reversed(range(0, 100))]

    start = time.time_ns()
    print(merge_sort(li))
    end = time.time_ns()

    print(f'Merge Sort took: {end - start}ns')

if __name__ == '__main__':
    main()