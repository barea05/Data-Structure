from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
        return self.container
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isempty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

s = Stack()
s.push(23)
print(s.push(55))
s.push(223)
s.push(2333)
s.push(23333)
# print(list(s))  TypeError: 'Stack' object is not iterable

print(s.container)
#print(s.push(23))
print(s.pop)
print(s.pop)
print(s.container.pop())
print(s.container)
print(s.size())
print(s.isempty())
print(s.container)
print(s.peek())

