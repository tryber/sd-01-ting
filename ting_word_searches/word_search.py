from ting_file_management.file_process import FileProcess
from ting_word_searches.factory import Factory
from ting_file_management.file_management import FileManagement
# Codigo feito junto com o DOuglas da Programação feito com sua orientação.


class SearchByWord:
    def __init__(self, path):
        self.path = path

    def search_by_word(self, word):
        main = FileManagement()
        file_process = FileProcess()
        file_process.process(self.path)
        lines = {"linha": line for line in main.fifo}
        answer = [Factory.dictionary(word, self.path, lines)]
        return answer
