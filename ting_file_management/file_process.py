from ting_file_management.file_management import txt_importer
from collections import deque # thx julio
import sys

queue = deque()


def process(path_file):
    data = txt_importer(path_file)
    if (data is None):
        return
    file_name = path_file.split('/')
    file = {
        'nome_do_arquivo': file_name[len(file_name) - 1],
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }
    if (file not in queue):
        queue.append(file)
        print(file, file=sys.stdout)


def remove():
    raise NotImplementedError


def file_metadata(position):
    raise NotImplementedError
