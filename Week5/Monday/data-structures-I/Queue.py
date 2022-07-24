####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:

    def __init__(self) -> None:
        self.base = []
        
    def enqueue(self, item):
        self.base.append(item)

    def dequeue(self):
        return self.base.pop(0)

    def peek(self):
        if self.base:
            return self.base[-1]
        return None

    def size(self):
        return len(self.base)

    def is_empty(self):
        if self.base:
            return False
        else:
            return True

def return_same(str):
    qu = Queue()
    results = ''
    for elm in str:
        qu.enqueue(elm)
    for i in range(len(str)):
        results += qu.dequeue()
    return results