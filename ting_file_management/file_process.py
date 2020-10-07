from ting_file_management.file_management import FileManagement
from ting_file_management.factory import Factory


# Projeto feito em pair programer com doug funny


class FileProcess:
    def __init__(self):
        self.main = FileManagement()
        self.path = ""

    def process(self, path_file):
        self.path = path_file
        try:
            self.main.txt_importer(path_file)
            amount_lines = len(self.main.fifo[0].split("\n"))
            answer = Factory.dictionary(
                path_file, amount_lines, len(self.main.fifo))
            print(answer)
            return answer

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
            answer = Factory.dictionary(self.path, amount_lines, position)
            return answer
        except ValueError:
            raise
