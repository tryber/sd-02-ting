OPTION_BACK = {"back": "Voltar ao menu anterior"}

OPTION_OUT = {"out": "Sair"}

MENU_PROCESS = [
    {"process": "Iniciar importação a partir de um arquivo TXT"},
    {"file_metadata": "Visualizar detalhes de arquivo anexado por posição"},
    {"remove": "Remover arquivo da base"},
    OPTION_BACK, OPTION_OUT
]

MENU_SEARCH = [
    {"exists_word": "Verificar se palavra existe na base"},
    {"search_by_word": "Buscar palavra em base"},
    OPTION_BACK, OPTION_OUT
]


MENU_MAIN = [
    {"menu_search": "Ir para o menu de busca"},
    {"menu process": "Ir para o menu de processos"},
    OPTION_OUT
]

MENUS = {
    "menu_search": MENU_SEARCH,
    "menu_process": MENU_PROCESS,
    "main": MENU_MAIN
}
