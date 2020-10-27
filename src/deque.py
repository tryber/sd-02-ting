class Deque:
    FIRST_ELEMENT = 1

    def __init__(self):
        self._data = [{
            'nome_do_arquivo': '',
            'qtd_linhas': 0,
            'conteudo_arquivo': []
        }]
        self._file_names = set()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Fila(" + ", ".join(map(lambda x: str(x), self._data)) + ")"

    def __iter__(self):
        return iter(self._data)

    def file_contains(self, file):
        return file in self._file_names

    def add_file_contains(self, file):
        return file in self._file_names

    def push_back(self, value):
        self._data.append(value)
        self._file_names.add(value['nome_do_arquivo'])

    def pop_front(self):
        if len(self._data) > 1:
            self._file_names.remove(
                self._data[self.FIRST_ELEMENT]['nome_do_arquivo']
            )
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def peek(self, position):
        if 0 < position < len(self._data):
            return self._data[position]
        else:
            return "Posição inválida"
