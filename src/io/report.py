
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    arquivo = open(path, 'w')
    arquivo.write(f'dataset: {config["type"]}\n \
                  path: {config["train_path"]}\n \
                  classifier: {config["classifier"]}\n \
                  training time per sample:{metrics_values}\n \
                  inference time per sample:{metrics_values}\n \
                  accuracy:{metrics_values}')

