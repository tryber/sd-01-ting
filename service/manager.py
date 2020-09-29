from os.path import isfile


class Manager:
    # def __init__(self):
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
            arquivo = open(path, "r")
            text = ""
            for phrase in arquivo:
                text += phrase
            arquivo.close()
            return text

        switcher = {"writer": writer, "reader": reader}
        return switcher.get(modifier, lambda: "método não implementado")()