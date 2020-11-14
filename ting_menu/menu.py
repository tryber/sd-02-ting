
from ting_menu.contants import MENUS
from ting_menu.services import create_menu


def menu():
    create_menu(MENUS["main"])


if __name__ == '__main__':
    menu()
