#--> Approaches to implement queue
#list
#collections.deque --> use queue and stack method
#queue.FifoQueue
stock_price = []
stock_price.insert(0, 123.123)
stock_price.insert(0, 123.123)
stock_price.insert(0, 123.123)
from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def deque(self):
        self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)

q = Queue()
print(q.buffer)
q.enqueue(23)
q.enqueue(2334)
q.enqueue(343)
print(q.buffer)
q.deque()
print(q.buffer)
print(q.is_empty())
print(q.size())