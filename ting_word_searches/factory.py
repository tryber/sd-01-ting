# Codigo feito com a ajuda do Henrique Eyer e do Doug Funny!

from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def dictionary(self):
        pass


class Factory(AbstractFactory):
    @staticmethod
    def dictionary(word, path_file, lines):
        return {
            "palavra": word,
            "arquivo": path_file,
            "ocorrencias": [line for line in lines],
        }
