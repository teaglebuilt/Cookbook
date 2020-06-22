


class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


input_str = "Hello"
output_str = "olleH"

#print(input_str[::-1])


def reverse_string(stack, string):
    # Loop through string and push chars
    for i in range(len(string)):
        stack.push(string[i])
    print(stack.items)

    output = ""
    while not stack.is_empty():
        output += stack.pop()
    print(output)
    return output


if __name__ == '__main__':
    reverse_string(Stack(), input_str)
