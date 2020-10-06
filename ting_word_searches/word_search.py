import sys
import re
# Colocar rota completa para o arquivo ting_file_management
# Exemplo /home/administrativo/sd-01-ting/ting_file_management
sys.path.append("colocar caminho do arquivo")

from file_process import FileProcess
from file_management import get_file_txt

file_process = FileProcess()
list_word_search = []


def exists_word(word, path_file):
    list_file = file_process.process(path_file)
    for search_file in list_file:
        lines = []

        list_file_content = get_file_txt(f"statics/{search_file['nome_do_arquivo']}")

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

        list_file_content = get_file_txt(f"statics/{search_file['nome_do_arquivo']}")

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


exists_word("de", "statics/arquivo_teste.txt")
search_by_word("de", "statics/arquivo_teste.txt")
