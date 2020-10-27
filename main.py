from src.deque import Deque
from ting_file_management.file_process import process, remove, file_metadata
from ting_word_searches.word_search import exists_word, search_by_word

project = Deque()

remove(project)
process(project, 'statics/teste_2.txt')
process(project, 'statics/teste_3.txt')
process(project, 'statics/arquivo_teste.txt')
process(project, 'statics/arquivo_teste.txt')
remove(project)
file_metadata(project, 3)
exists_word(project, 'vid')
search_by_word(project, 'de')
