from ting_file_management.file_management import txt_importer


file_names = {}


def process(path_file, queue):
    if (path_file in file_names):
            return
    file_names[path_file] = 1
    content = txt_importer(path_file)
    elem = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "content": content,
    }

    queue.insert(elem)


def remove(queue):
    return queue.pop()


def file_metadata(position, queue):
    return queue.search_position(position)
