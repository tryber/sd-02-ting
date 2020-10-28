from ting_file_management.file_process import file_queue
import re


def search_word(word, pattern):
    data = {}
    count_matchs = 0
    data['palavra'] = word
    for text in file_queue:
        data['arquivo'] = text['nome_do_arquivo']
        data['ocorrencias'] = []
        for index, lines in enumerate(text['linhas_do_arquivo']):
            if pattern.search(lines):
                data['ocorrencias'].append({'linha': index + 1})
                count_matchs += 1
    if (count_matchs == 0):
        return []
    return [data]


def search_by_word(word):
    raise NotImplementedError


def exists_word(word):
    if len(file_queue) == 0 or word.strip() == '':
        return []
    pattern = re.compile(rf"\b{word}\b", re.IGNORECASE)
    return search_word(word, pattern)
