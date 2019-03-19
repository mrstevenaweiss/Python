class Queue:

    # attributes
    def __init__(self):
        self.items = []

    # methods
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class Job:
    # attributes
    def __init__(self):
        pass

    # methods

class Printer:
    # attributes
    def __init__(self):
        pass

class PrinterQueue:
    # attributes
    def __init__(self):
        pass
