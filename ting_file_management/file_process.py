from ting_file_management.file_management import txt_importer
import sys


def process(class_instance, path_file):
    try:
        text = txt_importer(path_file)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
    if path_file in class_instance._file_names:
        print(f"Arquivo {path_file} já encontrado", file=sys.stderr)
        return
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "conteudo_arquivo": text,
    }
    class_instance.push_back(result)
    class_instance._file_names.add(path_file)
    print(result)
    return


def remove(class_instance):
    if class_instance.__len__() == 0:
        print('Não há o que remover!', file=sys.stderr)
        return
    item = class_instance.pop_front()
    class_instance._file_names.remove(item['nome_do_arquivo'])
    print(f'Arquivo {item["nome_do_arquivo"]} removido com sucesso')
    return


def file_metadata(position):
    raise NotImplementedError
