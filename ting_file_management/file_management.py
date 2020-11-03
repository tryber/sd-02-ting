import sys


def txt_importer(path_file):
    try:
        with open(path_file) as file:
            if not path_file.endswith(".txt"):
                return print("Formato inválido", file=sys.stderr)

            content = file.read()
            lines = content.splitlines()
            return lines

    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
