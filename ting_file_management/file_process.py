from file_management import txt_importer

# Código feito em pair programming com Coruja


class FileProcess:
    def __init__(self):
        self.list_file = []

    def process(self, path_file):
        get_read_file = txt_importer(path_file)
        if not isinstance(get_read_file, list):
            return get_read_file

        file_name = path_file.split("/")

        process_file = {
            "nome_do_arquivo": file_name[len(file_name) - 1],
            "qtd_linhas": len(get_read_file[0]),
            "posicao": len(get_read_file)
        }

        self.list_file.append(process_file)

        return self.list_file

    def remove(self, path_file):
        get_read_file = txt_importer(path_file)
        if not get_read_file:
            return "Arquivo não existe"

        try:
            del get_read_file[len(get_read_file) - 1]

            return f"Arquivo {path_file} removido."
        except IndexError:
            return f"Arquivo {path_file} não removido"

    def file_metadata(self, position, path_file):
        self.process(path_file)
        for item in self.list_file:
            if item["posicao"] == position:
                return item

        return "Posição inválida"
