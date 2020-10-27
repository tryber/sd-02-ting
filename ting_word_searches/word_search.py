def exists_word(class_instance, word):
    result = []
    for file in class_instance:
        file_read = {"palavra": word,
                     "arquivo": file['nome_do_arquivo'], "ocorrencias": []}
        for index, line in enumerate(file['conteudo_arquivo']):
            if word.lower() in line.lower():
                file_read['ocorrencias'].append({'linha': index+1})
        if file_read['ocorrencias']:
            result.append(file_read)
    print(result)
    return result


def search_by_word(class_instance, word):
    result = []
    for file in class_instance:
        file_read = {"palavra": word,
                     "arquivo": file['nome_do_arquivo'], "ocorrencias": []}
        for index, line in enumerate(file['conteudo_arquivo']):
            if word.lower() in line.lower():
                file_read['ocorrencias'].append(
                    {'linha': index+1, "conteudo": line}
                )
        if file_read['ocorrencias']:
            result.append(file_read)
    print(result)
    return result
