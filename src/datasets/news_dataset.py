
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
        self.palavras = []

        with open(path, 'r') as f:
            for line in f:
                news_name, news_class = line.split()
                news_name = news_name.split("/")
                self.news_name.append(news_name[1])
                self.news_class.append(news_class)

        if 'train' in path:
            """ identificar as palavras diferentes e salvar em um arquivo """
            palavras_escritas = []
            arquivo = open("src/datasets/todas_as_palavras", 'w')
            for i in range(len(self.news_name)):
                new_path = self.path[:-4] + "/" + self.news_name[i]
                todas_as_palavras = self.le_noticia(new_path)

                for p in todas_as_palavras:
                    if p not in palavras_escritas:
                        palavras_escritas.append(p)
                        arquivo.write(p + "\n")
            arquivo.close()

        with open('src/datasets/todas_as_palavras', 'r') as f:
            self.palavras = f.read().split()

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return int(len(self.news_name))

    def le_noticia(self, path):
        palavras_certas = []
        with open(path, 'r') as f:
            palavras = f.read().split()

        for i in range(len(palavras)):
            if palavras[i] not in stop_words:
                palavras_certas.append(palavras[i])

        return palavras_certas

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e a classe
        new_path = self.path[:-4] + "/" + self.news_name[idx]
        palavras = self.le_noticia(new_path)

        # inicializar vetor de frequencia com 0
        vetor_frequencia = []
        for i in self.palavras:
            vetor_frequencia.append(0)

        # usar o index pra incrementar a frequencia na posicao da palavra
        for i in palavras:
            if i in self.palavras:
                index = self.palavras.index(i)
                vetor_frequencia[index] += 1

        return vetor_frequencia, self.news_class[idx]
