from ting_file_management.file_process import queue


def search_by_word(word):
    results = []
    for file in queue:
        file_content = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_content["ocorrencias"].append({
                    "linha": index+1,
                    "conteudo": line
                })
        results.append(file_content)
    return results


def exists_word(word):
    results = []
    for file in queue:
        file_content = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_content["ocorrencias"].append({
                    "linha": index+1,
                })
        results.append(file_content)
    return results
