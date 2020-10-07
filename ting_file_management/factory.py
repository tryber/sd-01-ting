# Codigo feito com a ajuda do Henrique Eyer e do Doug Funny!

from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def dictionary(self):
        pass


class Factory(AbstractFactory):
    @staticmethod
    def dictionary(path_file, quantity_lines, position):
        return {
            "nome_do_arquivo": path_file,
            "qtd_linhas": quantity_lines,
            "posicao": position,
        }
