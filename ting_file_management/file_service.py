class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyNode("HEAD")
        self.tail = DoublyNode("TAIL")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.__length = 0

    def __len__(self):
        return self.__length

    def get_list(self):
        values_list = []
        position = 0
        if self.head.next != self.tail:
            current_node = self.head.next
            while position < len(self):
                values_list.append(current_node.value)
                current_node = current_node.next
                position += 1
        return values_list

    def get_node_at(self, position):
        node = None
        if self.head.next != self.tail:
            node = self.head.next
            while position > 0:
                node = node.next
                position -= 1
        return node

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        elif position >= len(self):
            return self.insert_last(value)
        node = DoublyNode(value)
        position_node = self.get_node_at(position)
        node.next = position_node
        node.previous = position_node.previous
        node.previous.next = node
        position_node.previous = node
        self.__length += 1

    def insert_first(self, value):
        node = DoublyNode(value)
        node.next = self.head.next
        node.previous = self.head
        node.next.previous = node
        self.head.next = node
        self.__length += 1

    def insert_last(self, value):
        node = DoublyNode(value)
        node.next = self.tail
        node.previous = self.tail.previous
        node.previous.next = node
        self.tail.previous = node
        self.__length += 1

    def is_empty(self):
        return not self.__length

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()
        remove_node = None
        if not self.is_empty():
            remove_node = self.get_node_at(position)
            remove_node_previous = remove_node.previous
            remove_node_next = remove_node.next
            remove_node_previous.next = remove_node_next
            remove_node.next = remove_node_previous
            remove_node.reset()
            self.__length -= 1
        return remove_node

    def remove_first(self):
        remove_node = None
        if not self.is_empty():
            remove_node = self.head.next
            remove_node_next = remove_node.next
            self.head.next = remove_node_next
            remove_node_next.previous = self.head
            remove_node.reset()
            self.__length -= 1
        return remove_node

    def remove_last(self):
        remove_node = None
        if not self.is_empty():
            remove_node = self.tail.previous
            remove_node_previous = remove_node.previous
            self.tail.previous = remove_node_previous
            remove_node_previous.next = self.tail
            remove_node.reset()
            self.__length -= 1
        return remove_node


class DoublyNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

    def reset(self):
        self.nest = None
        self.previous = None


def check_extension(path, expected_extension):
    if expected_extension not in path:
        raise ValueError("Formato inválido")


def create_double_list(data):
    file_list = DoublyLinkedList()
    for line in data:
        file_list.insert_last(line)
    return file_list


def file_not_found(path):
    file = path.split("/").pop()
    return "Arquivo {} não encontrado".format(file)


def get_file_name(file_path):
    return file_path.split("/").pop()
