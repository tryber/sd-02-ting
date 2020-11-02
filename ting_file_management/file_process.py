from ting_file_management.file_management import txt_importer
from collections import deque
import sys

queue = deque()


def process(path_file):
    content = txt_importer(path_file)
    if (content is None):
        return
    archive_name = path_file.split('/')
    archive = {
        'nome_do_arquivo': archive_name[len(archive_name) - 1],
        'qtd_linhas': len(content),
        'linhas_do_arquivo': content
    }
    if (archive not in queue):
        queue.append(archive)
        print(archive, file=sys.stdout)


def remove():
    if not len(queue) == 0:
        removed_file = queue.popleft()
        print(
            f'Arquivo {removed_file["nome_do_arquivo"]} removido com sucesso',
            file=sys.stdout
        )


def file_metadata(position):
    try:
        if(position == 0):
            raise Exception
        print(queue[position-1])
    except Exception:
        print('Posição inválida', file=sys.stderr)
