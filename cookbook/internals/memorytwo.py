
#   stack     heap
#             4
# __init__    Car{ wheels }
#   main

class Car:
    def __init__(self, w):
        self.wheels = w

    def getWheels(self):
        return self.wheels

# main
c = Car(4)
n = c.getWheels()
print(n)

"""The overall conclusion is that both stack and heap are used in pythons memory allocation. The way it works is from the main function up. Where main, the initial function is the first stack frame created. References to the frame are stored in heap. As a new function is called, a new stack frame is created which creates a new reference in the heap. The values in the heap are not over written if they are connected to a different stack frame, or scope of a function."""

"""As the functions resolve, the stack frames are removed til eventually we are back down to the main() stack frame."""

# Garbage Collection known as reference counting
"""The python interpreter has a table where it keeps track of the number of references to an object. The number of references change as do the variable assignments. If an object is left at 0, it is a dead object and removed from the heap."""
