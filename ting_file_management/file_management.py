list_file = []


def get_file_txt(path_file):
    try:
        with open(path_file, 'r') as f:
            lines = f.readlines()
            f.close()
            return lines
    except Exception:
        print(f"Arquivo {path_file} não encontrado")


def txt_importer(path_file):
    if path_file[-4::] != ".txt":
        print("Formato inválido")
        return "Formato inválido"

    reaf_file = get_file_txt(path_file)

    list_file.append(reaf_file)
    return list_file


txt_importer('statics/arquivo_teste.txt')
