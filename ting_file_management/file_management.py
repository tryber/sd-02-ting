import os
import sys


def check_path_and_format(file_name, file_ext):
    if not os.path.exists(file_name):
        print(f"Arquivo {file_name} não econtrado", file=sys.stderr)
        return True
    if not file_name.endswith(file_ext):
        print("Formato inválido", file=sys.stderr)
        return True
    return False


def txt_importer(path_file):
    lines_arr = []
    if check_path_and_format(path_file, '.txt'):
        return True
    with open(path_file, 'r') as file:
        for line in file:
            fields = line.split('\n')
            lines_arr.append(fields[0])
    return lines_arr
