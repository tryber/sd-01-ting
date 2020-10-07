from service.manager import Manager
# Codigo feito junto com o DOuglas da Programação feito com sua orientação.


class FileManagement:
    def __init__(self):
        self.fifo = []

    def txt_importer(self, path_file):
        main = Manager()
        if not main.valid_file_checker_and_extension(path_file):
            return None
        value = main.file_reader_and_writer("reader", path_file)
        self.fifo.append(value)
        print("importado com sucesso!")
