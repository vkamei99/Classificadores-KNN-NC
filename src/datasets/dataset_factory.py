
from typing import Dict
from .dataset_interface import DatasetInterface
from .image_dataset import ImageDataset
from .news_dataset import NewsDataset


def create_dataset(path: str, type: str) -> DatasetInterface:
    if type == 'image':
        return ImageDataset(path)
    elif type == 'news':
        return NewsDataset(path)
    else:
        raise Exception("Dataset type not found.")

"""
Essa função cria um objeto do tipo Dataset a partir dos argumentos "path" e "type".
Se o "type" for "image", a função retorna uma instância da classe ImageDataset, inicializada com "path".
Se o "type" for "news", a função retorna uma instância da classe NewsDataset, inicializada com "path".
Se o "type" não for encontrado, a função levanta uma exceção informando que o tipo de dataset não foi encontrado.
"""