from ting_file_management.file_service import (
    check_extension, DoublyLinkedList, file_not_found)


def txt_importer(path_file):
    check_extension(path_file, "txt")
    try:
        with open(path_file, "r") as txt_file:
            json_data = txt_file.readlines()
            file_list = DoublyLinkedList()
            for line in json_data:
                file_list.insert_last(line)
    except(FileNotFoundError):
        raise ValueError(file_not_found(path_file))
    else:
        return file_list
