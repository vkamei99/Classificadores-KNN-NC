from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar em uma lista
        self.path = path
        self.image_name = []
        self.image_class = []
        
        with open(path, 'r') as f:
            for line in f:
                image_name, image_class = line.split()
                self.image_name.append(image_name)
                self.image_class.append(image_class)

    def size(self) -> int:
        # retorna tamanho do dataset (numero de linhas do arquivo)
        return len(self.image_name)

    def get(self, idx: int) -> Tuple[Any, str]:
        # le a i-esima imagem do disco usando a biblioteca cv2 e retorna a imagem e a respectiva classe
        
        # "data/datasets/img/train(ou test).txt" --> "data/datasets/img/train/train(ou test)/"
        nome_pasta = self.path.split("/")[-1] #divide e seleciona o ultimo elemento da string (train.txt)
        nome_pasta = nome_pasta[:-4] #tira os 4 ultimos elementos da string
        
        new_path = self.path[:-4]
        new_path += /
        new_path = new_path + nome_pasta + / #"data/datasets/img/train/train(ou test)/"

        return 0, ""

'''
A interface de datasets define
que todos os datasets devem implementar os métodos size e get, sendo que o
primeiro retorna o número de amostras no dataset (número de imagens ou
notícias) e o segundo retorna o i-ésimo elemento em formato vetorial e a
respectiva classe.
'''
