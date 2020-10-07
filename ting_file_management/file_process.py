# Codigo feito com a ajuda do Henrique Eyer e do Doug Funny!

from ting_file_management.file_management import FileManagement
from ting_file_management.factory import Factory


class FileProcess:
    def __init__(self):
        self.main = FileManagement()
        self.path = ""

    def process(self, path_file):
        self.path = path_file
        try:
            self.main.txt_importer(path_file)
            amount_lines = len(self.main.fifo[0].split("\n"))
            result = Factory.dictionary(path_file, amount_lines, len(self.main.fifo))
            print(result)
            return result

        except ValueError:
            raise

    def remove(self):
        try:
            print("primeiro array", self.main.fifo)
            del self.main.fifo[0]
            print("segundo array", self.main.fifo)
        except IndexError:
            raise

    def file_metadata(self, position):
        try:
            amount_lines = len(self.main.fifo[position - 1].split("\n"))
            result = Factory.dictionary(self.path, amount_lines, position)
            return result
        except ValueError:
            raise
