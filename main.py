from src.deque import Deque
from ting_file_management.file_process import process, remove

project = Deque()

remove(project)
process(project, 'statics/arquivo_teste.txt')
process(project, 'statics/teste_2.txt')
process(project, 'statics/teste_3.txt')
# remove(project)

# print('peek', project.peek(0))
print('all', project.__str__())
