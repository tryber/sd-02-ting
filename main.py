from ting_file_management.file_process import process, remove, file_metadata
from ting_word_searches.word_search import search_by_word
from ting_file_management.Queue import Queue

queue = Queue()

process('./statics/arquivo_teste.txt', queue)

print(search_by_word('Acima', queue))
