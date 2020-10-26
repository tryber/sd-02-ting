import sys


def txt_importer(path_file):
    text_list = []
    with open(path_file, 'r') as text:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
            return
        content = text.read()
        for line in content.split('\n'):
            text_list.append(line)
    return text_list
