from ting_file_management.file_process import process, remove, file_metadata
from ting_file_management.Deque import Deque
from ting_word_searches.word_search import search_by_word, exists_word


project_instance = Deque()


remove(project_instance)
print('-------')
process('statics/arquivo_teste.txt', project_instance)
print('-------')
process('statics/file1.txt', project_instance)
print('-------')
process('statics/file2.txt', project_instance)
print('-------')
remove(project_instance)
print('------- >>>>>>>>>>>>>>>>>>>>')
file_metadata(project_instance, 0)
print('-------')
file_metadata(project_instance, 1)
print('-------')
file_metadata(project_instance, 2)
print('-------')
project_instance.peek_back()
print('------->>')
print(search_by_word('Pedro', project_instance))
print(exists_word('Pedro', project_instance))
