import os
import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não econtrado", file=sys.stderr)
        return
    text_list = []
    with open(path_file, 'r') as txt_file:
        txt_content = txt_file.read()
        for line in txt_content.split('\n'):
            text_list.append(line)
    return text_list
