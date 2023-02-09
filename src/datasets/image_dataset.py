from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2
import numpy as np
import time

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
                self.image_name.append(image_name[-7:])
                self.image_class.append(image_class)

    def size(self) -> int:
        # retorna tamanho do dataset (numero de linhas do arquivo)
        return int(len(self.image_name))

    def get(self, idx: int) -> Tuple[Any, str]:
        # le a i-esima imagem do disco usando a biblioteca cv2 e retorna a imagem e a respectiva classe
        
        new_path = self.path[:-4] + "/" + self.image_name[idx]#"data/datasets/img/train(ou test).txt" --> "data/datasets/img/train/image[idx]"

        img = cv2.imread(new_path, cv2.IMREAD_GRAYSCALE)#carrega a imagem em tons de cinza
        img_vector = np.ndarray.flatten(img)#transforma a imagem em vetor

        #printar as imagens na tela
        printar = True
        if printar:
            tempo_tela = 50
            start_time = time.time()
            img_larger = cv2.resize(img, (img.shape[1] * 10, img.shape[0] * 10), interpolation = cv2.INTER_CUBIC)
            if "train" in new_path:
                name = "Train"
            else:
                name = "Test"
            cv2.imshow(f"{name} Dataset", img_larger)
            while True:
                if (time.time() - start_time) * 1000 >= tempo_tela or cv2.waitKey(1) == 27:
                    break
            cv2.destroyAllWindows()

        return img_vector.tolist(), self.image_class[idx]

'''
A interface de datasets define
que todos os datasets devem implementar os métodos size e get, sendo que o
primeiro retorna o número de amostras no dataset (número de imagens ou
notícias) e o segundo retorna o i-ésimo elemento em formato vetorial e a
respectiva classe.
'''
