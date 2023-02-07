
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.train_amostras = []
        self.test_amostras = []
        self.tam_train = 0
        self.tam_test = 0

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset de treino
        self.tam_train = train_dataset.size()
        for i in range(self.tam_train):
            self.train_amostras.append(train_dataset.get(i))

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        
        K = 5
        distancia = []
        classes = []
        
        #guardando as amostras do test em uma lista
        self.tam_test = test_dataset.size()
        for i in range(self.tam_test):
            self.test_amostras.append(test_dataset.get(i))

        #calcula a distancia de todos os vetores
        for i in range(self.tam_test):
            for j in range(self.tam_train):
                somatorio = 0
                for x in range(len(self.test_amostras[i][0])):
                    somatorio += (self.train_amostras[j][0][x] - self.test_amostras[i][0][x]) ** 2
                dist = (somatorio)**1/2
                distancia.append((dist, self.train_amostras[j][1]))
        
        #ve os 5 pontos com menor distancia de cada teste e salva seus index em uma lista de listas
        # explicação abaixo*
        closest_k = []
        for i in range(self.tam_test):
            distances_for_sample = [(idx, d) for idx, d in enumerate(distancia) if idx // self.tam_train == i]
            distances_for_sample.sort(key=lambda x: x[1])
            closest_k.append([x[0] for x in distances_for_sample[:K]])

        classifier = []
        for indices in closest_k:
            class_count = {}
            for idx in indices:
                class_ = distancia[idx][1]
                if class_ not in class_count:
                    class_count[class_] = 0
                class_count[class_] += 1
            classifier.append(max(class_count, key=class_count.get))

        return classifier

        '''
        *A primeira parte encontra os índices das k distâncias mais próximas para cada amostra de teste. 
        Ela cria uma lista closest_k, onde cada elemento é uma lista de índices. 
        Esses índices são obtidos filtrando a lista de distâncias (distances) 
        e mantendo apenas aqueles que estão associados a cada amostra de teste (idx // self.train_size == i). 
        A lista resultante é então classificada pelo valor da distância (distances_for_sample.sort (key = lambda x: x [1])) 
        e os k índices mais próximos são selecionados (closest_k.append ([x [0] for x in distances_for_sample [: K]])).

        A segunda parte encontra a classe mais frequente entre os k vizinhos mais próximos. 
        Isso é feito percorrendo a lista closest_k e para cada lista de índices (indices) associados a cada amostra de teste, 
        ela conta quantas vezes cada classe aparece na lista de distâncias associada aos índices (class_count). 
        A classe com a contagem mais alta é determinada (classifier.append (max (class_count, key = class_count.get))) 
        e é adicionada a uma lista classifier. 
        
        Finalmente, a lista classifier é retornada como resultado da previsão.
        '''