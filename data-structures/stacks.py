class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        #accepts an item as a param and appends it to the end of the list. and returns nothing.
        # O(1) runtime
        self.items.append(item)

    def pop(self):
        #removes the last time for the list, which is also the top item
        #O(1) runtime
        return self.items.pop()

    def peek(self):
        # shows the last index in the list
        if self.items[-1]:
            return self.items[-1]
        return None

    def size(self):
        #removes the last time for the list, which is also the top item
        #O(1) runtime
        return len(self.items)

    def is_empty(self):
        return self.items == []
