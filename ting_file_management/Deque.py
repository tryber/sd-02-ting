class Deque:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []
        self.file_names = set()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Deque(" + ", ".join(map(lambda x: str(x), self._data)) + ")"

    def push_back(self, value):
        if value["nome_do_arquivo"] not in self.file_names:
            self._data.append(value)
            self.file_names.add(value["nome_do_arquivo"])
            print(value)

    def pop_front(self):
        if self._data:
            removed_element = self._data.pop(self.FIRST_ELEMENT)
            self.file_names.remove(removed_element["nome_do_arquivo"])
            print(f"Arquivo {removed_element['nome_do_arquivo']} removido com sucesso")
        else:
            print('Não há elementos')
        return None

    def peek_by_position(self, position):
        if 0 <= position < len(self._data):
            return self._data[position]
        return "Posição inválida"

    def peek_back(self):
        print(self._data)
        print(self.file_names)