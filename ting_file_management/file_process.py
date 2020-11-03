from ting_file_management.file_management import txt_importer
import sys


def process(path_file, deque):
    file_names = set([
        x["nome_do_arquivo"] for x in deque
    ])
    if path_file in file_names:
        return

    lines = txt_importer(path_file)
    if lines is None:
        return

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    deque.append(info)
    print(info, file=sys.stdout)


def remove(deque):
    if len(deque) > 0:
        removed = deque.popleft()
        path_file = removed["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(position, deque):
    try:
        info = deque[position]
        print(info, file=sys.stdout)
        return info
    except IndexError:
        print("Posição inválida", file=sys.stderr)
