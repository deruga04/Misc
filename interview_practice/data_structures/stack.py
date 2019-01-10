class Stack:
    def __init__(self):
        self.buffer = [None] * 10
        self.size = 0

    def push(self, x):
        if self.size < 10:
            self.buffer[self.size] = x
            self.size += 1
        else:
            print('Error, queue is full')

    def pop(self):
        if self.size > 0:
            self.buffer[self.size] = None
            self.size -= 1
        else:
            print('Error: No elements in queue')

    def peek(self):
        if self.size > 0:
            return self.buffer[self.size - 1]
        else:
            return None

s = Stack()
s.push(1)
print(s.peek())
s.push(2)
print(s.peek())
s.push(43)
print(s.peek())
s.pop()
print(s.peek())
