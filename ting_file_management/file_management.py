# Codigo feito com a ajuda do Henrique Eyer e do Doug Funny!

from service.manager import Manager


class FileManagement:
    def __init__(self):
        self.fifo = []

    def txt_importer(self, path_file):
        main = Manager()
        if not main.valid_file_checker_and_extension(path_file):
            return None
        value = main.file_reader_and_writer("reader", path_file)
        self.fifo.append(value)
        print("Importado com sucesso!")
