# Codigo feito com a ajuda do Henrique Eyer e do Doug Funny!

from ting_file_management.file_process import FileProcess
from ting_word_searches.factory import Factory
from ting_file_management.file_management import FileManagement


class SearchByWord:
    def __init__(self, path):
        self.path = path

    def search_by_word(self, word):
        main = FileManagement()
        file_process = FileProcess()
        file_process.process(self.path)
        lines = {"linha": line for line in main.fifo}
        result = [Factory.dictionary(word, self.path, lines)]
        return result
