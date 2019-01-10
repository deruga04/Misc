class Queue:
    def __init__(self):
        self.buffer = [None] * 10
        self.head = 0
        self.tail = 0

    def push(self, x):
        self.buffer[self.tail % 10] = x
        self.tail += 1
    
    def pop(self):
        r = self.buffer[self.head % 10]
        self.buffer[self.head] = None
        self.head += 1
        return r

    def peek(self):
        return self.buffer[self.head % 10]

q = Queue()
q.push(4)
print(q.peek())
q.push(6)
print(q.peek())
q.pop()
print(q.peek())
