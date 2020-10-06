import sys
import re
from file_process import FileProcess
from file_management import get_file_txt

# Código feito com ajuda de Coruja e Doug, o rei do paito

sys.path.append("colocar caminho do arquivo")


file_process = FileProcess()
list_word_search = []


def exists_word(word, path_file):
    list_file = file_process.process(path_file)
    for search_file in list_file:
        lines = []

        list_file_content = get_file_txt(
            f"statics/{search_file['nome_do_arquivo']}"
        )

        for phrase in list_file_content:
            if re.search(word, phrase, re.IGNORECASE):
                lines.append({"linha": list_file_content.index(phrase) + 1})

        dict_word_search = {
            "palavra": word,
            "arquivo": search_file["nome_do_arquivo"],
            "ocorrencias": lines
        }

        print(dict_word_search)


def search_by_word(word, path_file):
    list_file = file_process.process(path_file)
    for search_file in list_file:
        lines = []

        list_file_content = get_file_txt(
            f"statics/{search_file['nome_do_arquivo']}"
        )

        for phrase in list_file_content:
            if re.search(word, phrase, re.IGNORECASE):
                lines.append({
                    "linha": list_file_content.index(phrase) + 1,
                    "conteudo": re.sub("\n", "", phrase)
                })

        dict_word_search = {
            "palavra": word,
            "arquivo": search_file["nome_do_arquivo"],
            "ocorrencias": lines
        }

        print(dict_word_search)
