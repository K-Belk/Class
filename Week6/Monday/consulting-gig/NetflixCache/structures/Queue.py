class Queue:

    def __init__(self):
        self._base = []

    def enqueue(self, item):
        self._base.insert(0,item)

    def dequeue(self):
        return self._base.pop()

    def peek(self):
        return self._base[-1]

    def is_empty(self):
        return not self._base

    def peek_back(self):
        return self._base[0]