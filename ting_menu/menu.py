
from ting_menu.constants import MENUS
from ting_menu.services import create_menu


def menu():
    create_menu(MENUS["main"])


if __name__ == '__main__':
    menu()
