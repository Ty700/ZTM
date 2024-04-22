# Create a lambda expression that prints out a squared list

my_list = [1,2,3,4,5]

my_list = map(lambda item: item ** 2, my_list)

print(list(my_list))

# Create a lambda expression that sorts a tuple based on the 2nd value

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda x: x[1]) # The lambda is essentially saying the key is the 2nd element
print(list(a))

