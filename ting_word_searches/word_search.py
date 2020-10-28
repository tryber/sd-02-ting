from ting_file_management.file_process import file_queue
import re


def with_content_or_not(lines, idx, flag):
    if flag == 0:
        return {'linha': idx + 1}
    return {
            'linha': idx + 1,
            'conteudo': lines
        }


def search_word(word, pattern, flag):
    words_arr = []
    count_matchs = 0
    for text in file_queue:
        data = {}
        data['palavra'] = word
        data['arquivo'] = text['nome_do_arquivo']
        data['ocorrencias'] = []
        for index, lines in enumerate(text['linhas_do_arquivo']):
            if pattern.search(lines):
                data['ocorrencias'].append(
                    with_content_or_not(lines, index, flag
                    ))
                count_matchs += 1
        words_arr.append(data)
    if (count_matchs == 0):
        return []
    return words_arr


def search_by_word(word):
    if len(file_queue) == 0 or word.strip() == '':
        return []
    pattern = re.compile(rf"\b{word}\b", re.IGNORECASE)
    return search_word(word, pattern, 1)


def exists_word(word):
    if len(file_queue) == 0 or word.strip() == '':
        return []
    pattern = re.compile(rf"\b{word}\b", re.IGNORECASE)
    return search_word(word, pattern, 0)
