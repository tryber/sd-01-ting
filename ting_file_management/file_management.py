from services.manager import Manager

# Projeto feito em pair programer com doug funny


class FileManagement:
    def __init__(self):
        self.fifo = []

    def txt_importe(self, path_file):
        main = Manager()
        if not main.valid_file_checker(path_file):
            return None
        value = main.file_reader_writer("reader", path_file)
        self.fifo.append(value)
        print("importado com sucesso!")
