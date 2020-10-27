from ting_file_management.file_management import txt_importer
from collections import deque
import sys

file_queue = deque()
aux_queue = deque()


def process(path_file):
    process_file = {}
    data = txt_importer(path_file)
    split_path = path_file.split('/')
    process_file['nome_do_arquivo'] = split_path[len(split_path) - 1]
    process_file['qtd_linhas'] = len(data)
    process_file['linhas_do_arquivo'] = data
    if (process_file not in file_queue):
        file_queue.append(process_file)
        print('adicionado', file=sys.stdout)


def remove():
    if not len(file_queue) == 0:
        removed_file = file_queue.popleft()
        print(
            f'Arquivo {removed_file["nome_do_arquivo"]} removido com sucesso',
            file=sys.stdout
            )


def file_metadata(position):
    data = {}
    if position == 0 or len(file_queue) < position:
        print('Posição inválida', file=sys.stderr)
        return True
    for i in range(position):
        data = file_queue[i]
    # print(data)
    return data
