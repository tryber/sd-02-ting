from ting_file_management.file_service import (
    get_file_name, create_double_list, DoublyLinkedList)
from ting_file_management.file_management import txt_importer


def process(files_path):
    seen_names = {}
    for file_path in files_path:
        file_name = get_file_name(file_path)
        if file_name not in seen_names:
            seen_names[file_name] = True
            data = txt_importer(file_path)
            quantity_line = len(data)
            print({"nome_do_arquivo": file_name,
                   "qtd_linhas": quantity_line, "linhas_do_arquivo": data})


def remove():
    raise NotImplementedError


def file_metadata(position):
    raise NotImplementedError
