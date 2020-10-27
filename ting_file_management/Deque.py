class Deque:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []
        self.file_names = set()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def push_back(self, value):
        if value["nome_do_arquivo"] not in self.file_names:
            self._data.append(value)
            self.file_names.add(value["nome_do_arquivo"])
            print(value)

    def pop_front(self):
        if self._data:
            rm = self._data.pop(self.FIRST_ELEMENT)
            self.file_names.remove(rm["nome_do_arquivo"])
            print(
                f"Arquivo {rm['nome_do_arquivo']} removido com sucesso"
            )
        else:
            print("Não há elementos")
        return None

    def peek_by_position(self, position):
        if 0 <= position < len(self._data):
            return self._data[position]
        return "Posição inválida"

    def peek_back(self):
        print(self._data)
        print(self.file_names)
