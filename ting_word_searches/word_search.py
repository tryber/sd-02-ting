from ting_file_management.file_process import file_queue
import re


def search_by_word(word):
    raise NotImplementedError


def exists_word(word):
    if len(file_queue) == 0:
        return []
    pattern = re.compile(word, re.IGNORECASE)
    for text in file_queue:
        print(text['linhas_do_arquivo'])
