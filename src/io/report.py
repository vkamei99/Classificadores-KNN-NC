
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    arquivo = open(path, 'w')
    arquivo.write(f'Dataset: {config["type"]}\n'
                  f'Path: {config["train_path"]}\n' 
                  f'Classifier: {config["classifier"].upper()}\n' 
                  f'Training time per sample: {round(metrics_values["training_time_per_sample"], 4)}s\n' 
                  f'Inference time per sample: {round(metrics_values["inference_time_per_sample"], 4)}s\n' 
                  f'Accuracy: {round(metrics_values["accuracy"], 2)}\n\n'
                  #tradução pt-br ;)
                  f'Dataset: {config["type"]}\n'
                  f'Caminho: {config["train_path"]}\n' 
                  f'Classificador: {config["classifier"].upper()}\n' 
                  f'Tempo de treino por amostra: {round(metrics_values["training_time_per_sample"], 4)}s\n' 
                  f'Tempo de inferencia por amostra: {round(metrics_values["inference_time_per_sample"], 4)}s\n' 
                  f'Precisao: {round(metrics_values["accuracy"], 2)}'
                  )

