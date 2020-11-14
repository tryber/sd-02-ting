from ting_file_management.file_process import FileProcess
from ting_word_searches.word_service import (
    get_frequency_simple_report, get_frequency_complete_report)


class FileSearch(FileProcess):
    def __ini__(self):
        super().__init__()
        self.FILES_LIST = FileProcess.FILES_LIST

    # O(n)
    def exists_word(self, word):
        report = []
        files_list = self.FILES_LIST.get_list()
        for file in files_list:
            report.append({"palavra": word, "arquivo": file["name"],
                           "ocorrencias": get_frequency_simple_report(
                word, file["content"])})
        print(report)
        return report

    # O(n)
    def search_by_word(self, word):
        report = []
        files_list = self.FILES_LIST.get_list()
        for file in files_list:
            report.append({"palavra": word, "arquivo": file["name"],
                           "ocorrencias": get_frequency_complete_report(
                word, file["content"])})
        print(report)
        return report
