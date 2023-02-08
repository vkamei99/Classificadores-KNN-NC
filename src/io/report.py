
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    arquivo = open(path, 'w')
    arquivo.write(f'dataset: {config["type"]}\n'
                  f'path: {config["train_path"]}\n' 
                  f'classifier: {config["classifier"]}\n' 
                  f'training time per sample: {metrics_values["training_time_per_sample"]}s\n' 
                  f'inference time per sample: {metrics_values["inference_time_per_sample"]}s\n' 
                  f'accuracy: {metrics_values["accuracy"]}')

