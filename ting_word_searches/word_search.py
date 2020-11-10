import re
from ting_file_management.file_process import deque


def exists_word(word):
    files_search_result = []
    for file in deque:
        search_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        [
            search_result["ocorrencias"].append({"linha": index + 1})
            for index, line in enumerate(file["linhas_do_arquivo"])
            if re.match(f".*{word}.*", line, re.IGNORECASE)
        ]
        if search_result["ocorrencias"]:
            files_search_result.append(search_result)

    print(files_search_result)
    return files_search_result


def search_by_word(word):
    files_search_result = []
    for file in deque:
        search_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        [
            search_result["ocorrencias"].append(
                {"linha": index + 1, "conteúdo": line}
            )
            for index, line in enumerate(file["linhas_do_arquivo"])
            if re.match(f".*{word}.*", line, re.IGNORECASE)
        ]
        if search_result["ocorrencias"]:
            files_search_result.append(search_result)

    print(files_search_result)
    return files_search_result
