class Queue:
    def __init__(self):
        self.index = 0
        self.curr = 0
        self.queue = {}
        self.file_names = {}

    def insert(self, elem):
        self.queue[self.index] = elem
        self.index += 1

    def pop(self):
        elem = self.queue.pop(self.curr)
        self.curr += 1
        return elem

    def length(self):
        return self.index - self.curr

    def search_position(self, position):
        if (not self.queue[position]):
            return
        return self.queue[position]

    def interable(self):
        return self.queue.values()
