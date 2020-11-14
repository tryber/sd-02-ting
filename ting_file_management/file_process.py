from ting_file_management.file_service import (
    get_file_name, create_double_list, DoublyLinkedList)
from ting_file_management.file_management import txt_importer


class FileProcess():
    PROCESSED = {}

    FILES_LIST = DoublyLinkedList()

    @classmethod
    def process(cls, file_path):
        file_name = get_file_name(file_path)
        if file_name not in cls.PROCESSED:
            data = txt_importer(file_path)
            cls.PROCESSED[file_name] = True
            lines = '\n'.join(data)
            content_list = create_double_list(data)
            quantity_line = len(data)
            cls.FILES_LIST.insert_last(
                {"name": file_name,
                 "content": content_list})
            print(f"nome_do_arquivo: {file_name},\n\
qtd_linhas: {quantity_line},\n\
linhas_do_arquivo: \n{lines}")
            return {"nome_do_arquivo": file_name, "qtd_linhas": quantity_line,
                    "linhas_do_arquivo": lines}
        print(f"Arquivo {file_name} já processado")

    @classmethod
    def remove(cls):
        file = cls.FILES_LIST.remove_first()
        if file:
            file_name = file.value["name"]
            del cls.PROCESSED[file_name]
            print(f"Arquivo {file_name} removido com sucesso")

    @classmethod
    def file_metadata(cls, position):
        file = cls.FILES_LIST.get_node_at(position)
        if file:
            file_name = file.value["name"]
            lines = '\n'.join(file.value["content"].get_list())
            quantity_line = len(lines)
            return print(f"nome_do_arquivo: {file_name},\n\
qtd_linhas: {quantity_line},\n\
linhas_do_arquivo: \n{lines}")
        raise ValueError("Posição inválida")
