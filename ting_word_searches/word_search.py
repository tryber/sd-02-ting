from ting_file_management.file_process import queue


def add_case(file, file_read, word, need_content):
    for index, line in enumerate(file["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            if need_content:
                file_read["ocorrencias"].append({
                    "linha": index+1,
                    "conteudo": line
                })
            else:
                file_read["ocorrencias"].append({
                    "linha": index+1,
                })


def exists_word(word):
    result = []
    for file in queue:
        file_read = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        add_case(file, file_read, word, False)
        result.append(file_read)
    return result


def search_by_word(word):
    result = []
    for file in queue:
        file_read = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        add_case(file, file_read, word, True)
        result.append(file_read)
    return result
