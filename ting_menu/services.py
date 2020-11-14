import inquirer
# from ting_menu.contants import
from ting_file_management.file_process import FileProcess
from ting_word_searches.word_search import FileSearch
from ting_menu.contants import MENUS


def interface_back(create_menu, before_options):
    create_menu(before_options)


def interface_exists_word(create_menu, before_options):
    prompt_text(
        "Digite a palavra a ser consultada:",
        FileSearch,
        "exists_word",
    )
    create_menu(before_options)


def interface_file_metadata(create_menu, before_options):
    return prompt_text(
        "Digite a posição do arquivo a ser detalhado:",
        FileProcess,
        "file_metadata"
    )
    create_menu(before_options)


def interface_out():
    return print("Bolivar Say: GoodBye and Stay High")


def interface_process(create_menu, before_options):
    return prompt_text(
        "Digite o path do arquivo TXT a ser importado:",
        FileProcess,
        "process"
    )
    create_menu(before_options)


def interface_remove(create_menu, before_options):
    return prompt_text(
        "Digite Y para confirmar a remoção ou N para cancelar:",
        FileProcess,
        "remove"
    )
    create_menu(before_options)


def interface_search_by_word(create_menu, before_options):
    return prompt_text(
        "Digite a palavra a ser consultada:",
        FileSearch,
        "search_by_word"
    ),
    create_menu(before_options)


def prompt_confirm(message, callback_class, callback_method):
    interface = [inquirer.Confirm("remove", message=message)]
    value = inquirer.prompt(interface)
    if(value):
        callback_class[callback_method]()


def prompt_list(message, menu_options):
    interface = [inquirer.List(
        "option", message=message, choices=menu_options)]
    return inquirer.prompt(interface)["option"]


def prompt_text(message, callback_class, callback_method):
    interface = [inquirer.Text("option", message=message)]
    value = inquirer.prompt(interface)["option"]
    if value:
        return callback_class[callback_method](value)
    return callback_class[callback_method]()


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
    option = prompt_list(
        "Welcome to Bolivar Ting - Choose a Menu", menu_options)
    isMenu = option.split("_")[0] == "menu"
    if isMenu:
        create_menu(MENUS[option])
    else:
        INTERFACES[option](create_menu, menu_options)
