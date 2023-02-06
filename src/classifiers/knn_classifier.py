
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
        
        k = 5
        #guardando as amostras do test em uma lista
        self.tam_test = test_dataset.size()
        for i in range(self.tam_test):
            self.test_amostras.append(test_dataset.get(i))
        
        



        return []
