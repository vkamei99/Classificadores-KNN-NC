
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
from .stopwords import *

class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        self.path = path
        self.news_name = []
        self.news_class = []

        with open(path, 'r') as f:
            for line in f:
                news_name, news_class = line.split()
                self.news_name.append(news_name[-17:])
                self.news_class.append(news_class)

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return int(len(self.news_name))

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e a classe
        palavras = []
        new_path = self.path[:-4] + "/" + self.news_name[idx]
        with open(new_path, 'r') as f:
            for linha in f:
                palavras.append(linha.split())


        return palavras, ""
