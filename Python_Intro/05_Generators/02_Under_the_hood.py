# Under the hood of a generator

# # This is essentially how a loop works:
def special_for(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator) * 2)
        except StopIteration:
            break

special_for([1,2,3])

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self): 
        return self

    def __next__(self):
        if MyGen.current < self.last:
            number = MyGen.current
            MyGen.current += 1
            return number
        raise StopIteration # If MyGen.current (current value of generator) ! < self.last throw out of index error

gen = MyGen(0,100)

for i in gen:
    print(i)

