from collections import deque as Deque
from ting_file_management.file_process import process, remove, file_metadata
from ting_word_searches.word_search import exists_word, search_by_word

deque = Deque()

process("arquivo_nao_existente.txt", deque)
process("statics/arquivo_nao_txt.json", deque)

process("statics/novo_paradigma_globalizado-min.txt", deque)
process("statics/arquivo_teste.txt", deque)
process("statics/arquivo_teste.txt", deque)

file_metadata(0, deque)
file_metadata(1, deque)
file_metadata(2, deque)

exists_word("variáveis", deque)
exists_word("tudo", deque)
exists_word("cassio", deque)

search_by_word("Variáveis", deque)
search_by_word("tuDo", deque)
search_by_word("cassiO", deque)

remove(deque)
remove(deque)
remove(deque)
