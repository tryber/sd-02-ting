from ting_file_management.file_management import txt_importer


def process(path_file, queue):
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
