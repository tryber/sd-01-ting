from service.manager import Manager

# código feito com o auxílio do Doug Funny, mais conhecido como douglas da programação


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
