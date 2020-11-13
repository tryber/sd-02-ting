from constants import (expected_data, path_arquivo_teste,
                       path_json_format, path_not_exist)
from ting_file_management.file_management import txt_importer
import pytest


def test_txt_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo not_exist.txt não encontrado"):
        txt_importer(path_not_exist)


def test_txt_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        txt_importer(path_json_format)


def test_txt_importer_on_success():
    data = txt_importer(path_arquivo_teste)
    assert data == expected_data
