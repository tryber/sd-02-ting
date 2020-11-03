from collections import deque as Deque
from ting_file_management.file_process import process, remove, file_metadata

deque = Deque()

process("arquivo_nao_existente.txt", deque)
process("statics/arquivo_nao_txt.json", deque)
print(deque)

process("statics/novo_paradigma_globalizado-min.txt", deque)
process("statics/arquivo_teste.txt", deque)
process("statics/arquivo_teste.txt", deque)
print(deque)

remove(deque)
remove(deque)
remove(deque)
print(deque)

process("statics/arquivo_teste.txt", deque)
file_metadata(0, deque)
file_metadata(1, deque)
