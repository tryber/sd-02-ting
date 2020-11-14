import inquirer
# from ting_menu.contants import
from ting_file_management.file_process import FileProcess
from ting_word_searches.word_search import FileSearch
from ting_menu.constants import MENUS


def interface_back(create_menu, before_options):
    create_menu(before_options)


def interface_exists_word(create_menu, before_options):
    prompt_text(
        "Digite a palavra a ser consultada",
        FileSearch,
        "exists_word",
    )
    create_menu(before_options)


def interface_file_metadata(create_menu, before_options):
    position = prompt_text("Digite a posição do arquivo a ser detalhado")
    FileProcess.file_metadata(int(position))
    create_menu(before_options)


def interface_out():
    return print("Bolivar Say: GoodBye and Stay High")


def interface_process(create_menu, before_options):
    path = prompt_text("Digite o path do arquivo TXT a ser importado")
    FileProcess.process(path)
    create_menu(before_options)


def interface_remove(create_menu, before_options):
    remove = prompt_confirm(
        "Digite Y para confirmar a remoção ou N para cancelar",
    )
    if remove:
        FileProcess.remove()
    create_menu(before_options)


def interface_search_by_word(create_menu, before_options):
    instance = FileSearch()
    word = prompt_text("Digite a palavra a ser consultada")
    instance.search_by_word(word)
    create_menu(before_options)


def prompt_confirm(message):
    interface = [inquirer.Confirm("option", message=message)]

    return inquirer.prompt(interface)["option"]


def prompt_list(message, menu_options):
    interface = [inquirer.List(
        "option", message=message, choices=menu_options)]
    return inquirer.prompt(interface)["option"]


def prompt_text(message):
    interface = [inquirer.Text("option", message=message)]
    return inquirer.prompt(interface)["option"]


INTERFACES = {
    "back": interface_back,
    "exists_word": interface_exists_word,
    "file_metadata": interface_file_metadata,
    "out": interface_out,
    "process": interface_process,
    "remove": interface_remove,
    "search_by_word": interface_search_by_word
}


def create_menu(menu_options):
    option_values = []
    option_keys = []
    for option in menu_options:
        option_keys.append(option[0])
        option_values.append(option[1])
    option_value = prompt_list(
        "Welcome to Bolivar Ting - Choose a Menu", option_values)
    option_key = option_keys[option_values.index(option_value)]
    isMenu = option_key.split("_")[0] == "menu"
    if isMenu:
        create_menu(MENUS[option_key])
    else:
        INTERFACES[option_key](create_menu, menu_options)
