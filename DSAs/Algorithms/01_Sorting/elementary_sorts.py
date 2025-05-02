# Bubble, Selection, and Insertion 

# Bubble    - "Bubbles" the "greatest" element in the list to the top of the list
# Selection - Selects the "smallest" element in the list and puts it to the first index
# Insertion - Useful for when you are pretty sure the list is almost -> already sorted
#           - Best case scenario is O(n)
#           - Preforms well with small datasets

import time

li = [x for x in reversed(range(0, 100))]
li2 = [x for x in reversed(range(0, 100))]
li3 = [x for x in reversed(range(0, 100))]

def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                # Swap
                li[j], li[j+1] = li[j+1], li[j]
    return li

def selection_sort(li):
    length = len(li)

    for i in range(length):
        min = None
        for j in range(i, length):
            if min == None:
                min = j
            else:
                if li2[j] < li2[min]:
                    min = j
        li2[i], li2[min] = li2[min], li2[i]
    return li2

def insertion_sort(li):
    for i in range(len(li)):
        if li[i] < li[0]:
            val = li.pop(i)
            li.insert(0, val)
        else:
            for j in range(1, i):
                if li[i] > li[j-1] and li[i] < li[j] :
                    val = li.pop(i)
                    li.insert(j, val)
    return li
        

start = time.time_ns()
print(bubble_sort(li))
end = time.time_ns()
print('It took %.2f ns' % ((end - start)))

start = time.time_ns()
print(selection_sort(li2))
end = time.time_ns()
print('It took %.2f ns' % ((end - start)))


start = time.time_ns()
print(insertion_sort(li3))
end = time.time_ns()
print('It took %.2f ns' % ((end - start)))