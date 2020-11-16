
from ting_menu.constants import MENU_MAIN
from ting_menu.services import create_menu


def menu():
    create_menu(MENU_MAIN)


if __name__ == '__main__':
    menu()
