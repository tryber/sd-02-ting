from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    result = txt_importer(path_file)
    returned_object = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(result),
        "linhas_do_arquivo": result,
    }
    instance.push_back(returned_object)


def remove(instance):
    instance.pop_front()


def file_metadata(instance, position):
    print(instance.peek_by_position(position))
