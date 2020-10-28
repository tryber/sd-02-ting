import sys
import os


def check_file_extention(filename, extention):
    if os.path.splitext(filename)[1] != extention:
        raise ValueError("Formato inválido")


def txt_importer(path_file):
    try:
        check_file_extention(path_file, '.txt')

        with open(path_file) as file:
            content = file.read()
            return content.split('\n')

    except ValueError as exc:
        print(exc, file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
