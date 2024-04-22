# Add code in SuperClass() that makes it act as a list
# len() returns 1000 no matter what
# How can we easily aquire the power of a normal list, but modify the len dunder

class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()
super_list.append(5)

print(super_list[0])
print(len(super_list))

# This will print True or False depending if the left argument inherits from the right argument
# Arguments must be an object type
print(issubclass(SuperList, object))