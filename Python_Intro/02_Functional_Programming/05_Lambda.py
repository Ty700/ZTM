from functools import reduce
# Lambda Expressions
    # One time functions that are anonymous and you don't need more than once
    # Useful for when you need a function that:
        # Only use once
        # Anonymous functions <= no name for them to call later

# Example:

# lambda parameter: action(parameter)

# Multiple by 2 Example:

my_list = [1,2,3,4,5]

new_list = map(lambda item: item*2, my_list)

print(my_list)
print(list(new_list))

# Filtering Example
filtered_list = filter(lambda item: (item % 2 == 0), my_list)

print(list(filtered_list))

# Reducing Example

reduced_list = reduce(lambda acc, item: item + acc, my_list, 0)
print(reduced_list)