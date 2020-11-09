import sys


def check_file_extension(file):
    if not file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return False
    return True


def txt_importer(path_file):
    try:
        with open(path_file, "r") as text:
            if check_file_extension(path_file):
                return [line.split('\n')[0] for line in text]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
