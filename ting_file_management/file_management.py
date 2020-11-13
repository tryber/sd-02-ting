from ting_file_management.file_service import (check_extension, file_not_found)


def txt_importer(path_file):
    check_extension(path_file, "txt")
    try:
        with open(path_file, "r") as txt_file:
            json_data = txt_file.readlines()
    except(FileNotFoundError):
        raise ValueError(file_not_found(path_file))
    else:
        return json_data
