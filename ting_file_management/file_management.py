list_file = []


def txt_importer(path_file):
    if path_file[-4::] != ".txt":
        print("Formato inválido")
        return "Formato inválido"
    try:
        with open(path_file, 'r') as f:
            lines = f.readlines()
            f.close()
            list_file.append(lines)
            return list_file
    except Exception:
        print(f"Arquivo {path_file} não encontrado")


# txt_importer('statics/arquivo_teste.txt')
