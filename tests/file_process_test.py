from constants import (expected_data, expected_process, path_arquivo_teste,
                       path_json_format, path_other_test,  path_not_exist)
from ting_file_management.file_process import FileProcess


def test_process_on_success(capsys):
    file = FileProcess()
    file.process([path_arquivo_teste, path_other_test])
    out, err = capsys.readouterr()
    assert out == expected_process


def test_ignore_same_name_files(capsys):
    file = FileProcess()
    file.process([path_arquivo_teste, path_other_test, path_arquivo_teste])
    out, err = capsys.readouterr()
    assert out == expected_process
