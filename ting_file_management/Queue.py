class Queue:
    def __init__(self):
        self.index = 0
        self.curr = 0
        self.queue = {}
        self.file_names = {}

    def insert(self, elem):
        if (elem["nome_do_arquivo"] in self.file_names):
            return
        self.queue[self.index] = elem
        self.index += 1
        self.file_names[elem["nome_do_arquivo"]] = 1

    def pop(self):
        elem = self.queue[self.curr]
        self.curr += 1
        return elem

    def length(self):
        return self.index - self.curr

    def search_position(self, position):
        if (not self.queue[position]):
            return
        return self.queue[position]

    def interavel(self):
        return self.queue.values()
