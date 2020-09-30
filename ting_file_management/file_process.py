from file_management import txt_importer


def process(path_file):
    get_read_file = txt_importer(path_file)
    if not isinstance(get_read_file, list):
        return get_read_file

    file_name = path_file.split("/")

    process_file = {
        "nome_do_arquivo": file_name[len(file_name) - 1],
        "qtd_linhas": len(get_read_file[0]),
        "posicao": len(get_read_file)
    }

    print(process_file)

    return process_file


def remove():
    raise NotImplementedError


def file_metadata(position):
    raise NotImplementedError


process('statics/arquivo_teste.txt')
