import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r") as file:
            if not path_file.endswith(".txt"):
                raise ValueError
            file_split = file.read().split(sep="\n")
            return file_split
        print("Importação realizada com sucesso", file=sys.stdout)

    except ValueError:
        print("Formato inválido", file=sys.stderr)
        sys.exit(1)

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        sys.exit(1)
