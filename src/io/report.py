import pandas as pd
import os
from typing import Dict

def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    # Escreve o relatório do experimento
    with open(path, 'w') as arquivo:
        arquivo.write(f'Dataset: {config["type"]}\n'
                      f'Path: {config["train_path"]}\n' 
                      f'Classifier: {config["classifier"].upper()}\n' 
                      f'Training time per sample: {round(metrics_values["training_time_per_sample"], 4)}s\n' 
                      f'Inference time per sample: {round(metrics_values["inference_time_per_sample"], 4)}s\n' 
                      f'Accuracy: {round(metrics_values["accuracy"], 2)}\n\n'

                      # tradução pt-br ;)
                      f'Dataset: {config["type"]}\n'
                      f'Caminho: {config["train_path"]}\n' 
                      f'Classificador: {config["classifier"].upper()}\n' 
                      f'Tempo de treino por amostra: {round(metrics_values["training_time_per_sample"], 4)}s\n' 
                      f'Tempo de inferencia por amostra: {round(metrics_values["inference_time_per_sample"], 4)}s\n' 
                      f'Precisao: {round(metrics_values["accuracy"], 2)}\n\n')
    
    # Caminho para o arquivo CSV de histórico
    csv_path = os.path.join(os.path.dirname(path), 'reports.csv')

    # Dicionário com os dados atuais
    novo_dado = {
        "Dataset": config["type"],
        "Train Path": config["train_path"],
        "Test Path": config["test_path"],
        "Classificador": config["classifier"].upper(),
        "Tempo de treino por amostra": round(metrics_values["training_time_per_sample"], 4),
        "Tempo de inferencia por amostra": round(metrics_values["inference_time_per_sample"], 4),
        "Precisao": (metrics_values["accuracy"])
    }

    # Verifica se o arquivo CSV já existe
    if os.path.exists(csv_path):
        # Se existir, lê o arquivo existente e adiciona o novo registro
        df = pd.read_csv(csv_path)
        df = pd.concat([df, pd.DataFrame([novo_dado])], ignore_index=True)
    else:
        # Se não existir, cria um novo DataFrame com o novo registro
        df = pd.DataFrame([novo_dado])

    # Salva o DataFrame atualizado de volta no arquivo CSV
    df.to_csv(csv_path, index=False)

