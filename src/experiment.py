
from typing import Union, Dict, List
from src.datasets.dataset_interface import DatasetInterface
from src.classifiers.classifier_interface import ClassifierInterface
from src.metrics import accuracy
import time


class Experiment:
    def __init__(self,
                 train_dataset: DatasetInterface,
                 test_dataset: DatasetInterface):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.true_classes = self._get_true_classes_from_dataset(
            self.test_dataset)

    def run(self, classifier: ClassifierInterface) -> Dict[str, float]:
        """ executa o experimento """
        treino_t = time.time()
        classifier.train(self.train_dataset)
        treino_to = time.time()

        predicit_t = time.time()
        pred_classes = classifier.predict(self.test_dataset)
        predicit_to = time.time()

        metrics = {
            "accuracy": accuracy(self.true_classes, pred_classes),
            "training_time_per_sample": (treino_to - treino_t)/self.test_dataset.size(),
            "inference_time_per_sample": (predicit_to-predicit_t)/self.train_dataset.size(),
        }

        return metrics

    def _get_true_classes_from_dataset(self, dataset: DatasetInterface) -> List[str]:
        true_classes = []
        for idx in range(dataset.size()):
            _, sample_class = dataset.get(idx)
            true_classes.append(sample_class)
        return true_classes
