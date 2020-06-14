


"""
Python program begins its execution under main method stack. The objects are created in heap memory and the references are created in stack memory. Even though f1 and f2 have same values, they do not overwrite since they are in seperate stacks."""

"""On completion of code evaluation, the stack frame is removed from memory if no longer required. So we are left with one stack frame of main. But what happens to the objects in the heap?"""


# stack  heap
# f2 x --> 11
# f1 x --> 10
# main y --> 5


def f2(x):
    x = x + 1 # in heap as 11
    return x

def f1(x):
    x = x * 2 # in heap as 10
    y = f2(x)
    return y


def main():
    y = 5
    z = f1(y) # not in heap. the lower main from holds the state of method and the line thats executed.


if __name__ == '__main__':
    main()
