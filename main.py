from src.deque import Deque
from ting_file_management.file_process import process, remove, file_metadata

ting = Deque()

process(ting, "./statics/arquivo_teste.txt")
process(ting, "./statics/teste2")
process(ting, "./statics/teste2.txt")
process(ting, "./statics/teste3.txt")
remove(ting)
file_metadata(ting, 0)
