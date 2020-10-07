# Codigo feito com a ajuda do Henrique Eyer e do Doug Funny!

from os.path import isfile


class Manager:
    def valid_file_checker_and_extension(self, path_file):
        if not path_file.endswith(".txt"):
            print("Formato inválido")
            return False
        if not isfile(path_file):
            print(f"Arquivo {path_file} não encontrado")
            return False
        return True

    def file_reader_and_writer(self, modifier, path, files=None):
        def writer():
            with open(path, "a") as txt_file:
                txt_file.write(files)
            return txt_file.close()

        def reader():
            archive = open(path, "r")
            text = ""
            for phrase in archive:
                text += phrase
            archive.close()
            return text

        switcher = {"writer": writer, "reader": reader}
        return switcher.get(modifier, lambda: "método não implementado")()
