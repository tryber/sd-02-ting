from ting_file_management.file_service import (
    get_file_name, create_double_list, File)
from ting_file_management.file_management import txt_importer


class FileProcess(File):
    def __ini__(self):
        super().__init__()

    def process(self, files_path):
        seen_names = {}
        for file_path in files_path:
            file_name = get_file_name(file_path)
            if file_name not in seen_names:
                seen_names[file_name] = True
                data = txt_importer(file_path)
                content_list = create_double_list(data)
                quantity_line = len(data)
                print({"nome_do_arquivo": file_name,
                       "qtd_linhas": quantity_line, "linhas_do_arquivo": data})
                self.files_list.insert_last(
                    {"name": file_name,
                     "content": content_list})

    def remove(self):
        file = self.files_list.remove_first()
        if file:
            print(f"Arquivo {file.name} removido com sucesso")

    def file_metadata(self, position):
        file = self.files_list.get_node_at(position)
        if file:
            return print({"nome_do_arquivo": file.value.name,
                          "qtd_linhas": len(file),
                          "linhas_do_arquivo": file.content.get_list()})
        raise ValueError("Posição inválida")
