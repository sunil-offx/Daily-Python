from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
