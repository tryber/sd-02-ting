import inquirer
# from ting_menu.contants import
from ting_file_management.file_process import FileProcess
from ting_word_searches.word_search import FileSearch
from ting_menu.constants import (MENUS, MENU_MAIN, MENUS_ACCESS)


def interface_back(create_menu, menu_options):
    menus = MENUS_ACCESS.get_list()
    menu_index = menus.index(menu_options)
    create_menu(menus[menu_index - 1])


def interface_exists_word(create_menu, menu_options):
    word = prompt_text("Digite a palavra a ser consultada")
    try:
        instante = FileSearch()
        instante.exists_word(word)
    except Exception as err:
        print("ERROR", err)
    finally:
        create_menu(menu_options)


def interface_file_metadata(create_menu, menu_options):
    position = prompt_text("Digite a posição do arquivo a ser detalhado")
    try:
        FileProcess.file_metadata(int(position))
    except Exception as err:
        print("ERROR", err)
    finally:
        create_menu(menu_options)


def interface_out(create_menu, menu_options):
    return print("xoxo xoxo xoxo xoxo xoxo xoxo")


def interface_process(create_menu, menu_options):
    path = prompt_text("Digite o path do arquivo TXT a ser importado")
    try:
        FileProcess.process(path)
    except Exception as err:
        print("ERROR", err)
    finally:
        create_menu(menu_options)


def interface_remove(create_menu, menu_options):
    remove = prompt_confirm(
        "Digite Y para confirmar a remoção ou N para cancelar",
    )
    if remove:
        FileProcess.remove()
    create_menu(menu_options)


def interface_search_by_word(create_menu, menu_options):
    word = prompt_text("Digite a palavra a ser consultada")
    try:
        instante = FileSearch()
        instante.search_by_word(word)
    except Exception as err:
        print("ERROR", err)
    finally:
        create_menu(menu_options)


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
    MENUS_ACCESS.insert_first(menu_options)
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
