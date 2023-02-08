from typing import List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
from math import dist

class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.data_points = []#armazena todos os pontos de dados do conjunto de treinamento
        self.centroids = []#armazena os centroides calculados para cada classe
        self.classes = []#classes únicas
        self.data_vectors = []#é uma lista de listas que contém os pontos de dados para cada classe
        self.test_data = []#armazena os dados de teste
        
    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        # Armazenando todos os dados de treinamento na lista data_points
        for i in range(train_dataset.size()):
            self.data_points.append(train_dataset.get(i))

        # Armazenando todas as classes dos dados de treinamento na lista classes
        for point in self.data_points:
            if point[1] not in self.classes:
                self.classes.append(point[1])

        # Armazenando os vetores de dados na lista data_vectors
        for class_name in self.classes:
            class_points = []
            for point in self.data_points:
                if point[1] == class_name:
                    class_points.append(point[0])
            self.data_vectors.append(class_points)

        # Cálculo dos centróides a partir dos vetores de dados
        for class_vectors in self.data_vectors:
            centroid = []
            for j in range(len(class_vectors[0])):
                sum_of_vectors = sum(vector[j] for vector in class_vectors)
                centroid.append(sum_of_vectors / len(class_vectors))
            self.centroids.append(centroid)

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        # Armazenando todos os dados de teste na lista test_data
        self.test_data = [test_dataset.get(i) for i in range(test_dataset.size())]

        # Lista que armazena as classes previstas
        predicted_classes = []

        # Loop que itera sobre cada ponto de teste
        for test_point in self.test_data:
            min_distance = float('inf') #armazena a distância mínima
            closest_centroid_index = 0  #armazena o índice do centróide mais próximo
            
            # Loop por todos os centroides
            for i, centroid in enumerate(self.centroids):
                distance = dist(test_point[0], centroid)# Cálculo da distância euclidiana

                # Verifica se a distância é menor que a distância mínima
                if distance < min_distance:
                    min_distance = distance
                    closest_centroid_index = i
                    
            predicted_classes.append(self.classes[closest_centroid_index])
                        
        return predicted_classes
