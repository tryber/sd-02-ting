import sys
from os import path
from file_management import txt_importer


def process(path_file):
    exist = path.exists(path_file) or path.exists(f"./{path_file}")
    list_text = []
    line_count = 0

    if not exist:
        print(f"Arquivo {path_file} não existe", file=sys.stderr)
        return
    if not path_file.endswith(".txt"):
        print("Formato Inválido", file=sys.stderr)
        return

    text_read = txt_importer(path_file)

    for line in text_read:
        line_count += 1
    list_text.append({
        "nome_do_arquivo": path_file,
        "qtd_linhas": line_count,
        "linhas do arquivo": text_read
    })

    return list_text


def remove():
    raise NotImplementedError


def file_metadata(position):
    raise NotImplementedError


print(process("./statics/arquivo_teste.txt"))
