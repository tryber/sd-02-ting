class Deque:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()
        self._file_names = set()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Fila(" + ", ".join(map(lambda x: str(x), self._data)) + ")"

    # def push_front(self, value):
    #     self._data.insert(self.FIRST_ELEMENT, value)

    def push_back(self, value):
        self._data.append(value)

    def pop_front(self):
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    # def pop_back(self):
    #     if self._data:
    #         return self._data.pop()
    #     return None

    def peek_front(self):
        if self._data:
            return self._data[self.FIRST_ELEMENT]
        return None

    def clear(self):
        self._data = list()

    def exists(self, value):
        return value in self._data

    
