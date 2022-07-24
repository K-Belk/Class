####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

from ast import Str


class Stack:

    def __init__(self):
        self.base = []

    def push(self, item):
        self.base.append(item)

    def pop(self):
        return self.base.pop()

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


def reverse(str):
    st = Stack()
    results = ''
    for elm in str:
        st.push(elm)
    for i in range(len(str)):
        results += st.pop()
    return results
