def exists_word(word, deque):
    file_results = []
    for item in deque:
        line_results = []
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                line_results.append({
                    "linha": index + 1,
                })
        if len(line_results) > 0:
            file_results.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": line_results,
            })
    print(file_results)
    return file_results


def search_by_word(word, deque):
    file_results = []
    for item in deque:
        line_results = []
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                line_results.append({
                    "linha": index + 1,
                    "conteudo": line,
                })
        if len(line_results) > 0:
            file_results.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": line_results,
            })
    print(file_results)
    return file_results
