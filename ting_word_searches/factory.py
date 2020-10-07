from abc import ABC, abstractmethod
# Codigo feito junto com o DOuglas da Programação feito com sua orientação.


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
