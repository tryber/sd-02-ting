from ting_file_management.file_management import txt_importer
from collections import deque as Deque


deque = Deque()


def process(path_file):
    text_lines = txt_importer(path_file)
    file_process = {
        "nome_do_arquivo": path_file.split("/")[-1],
        "qtd_linhas": len(text_lines),
        "linhas_do_arquivo": text_lines
    }
    if file_process not in deque:
        deque.append(file_process)
        print(file_process)


def remove():
    raise NotImplementedError


def file_metadata(position):
    raise NotImplementedError
