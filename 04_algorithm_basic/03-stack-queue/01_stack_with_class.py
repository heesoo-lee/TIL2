class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, item):
        self.top += 1
        self.items[self.top] = item

    def is_full(self):

        return self.capacity == self.top

    
stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.pop())
# print(stack.pop())
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.pop())
