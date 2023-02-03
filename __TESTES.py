from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.args import parse_args
import argparse
from src.io.config import load_config
from src.io.report import write_report

def main():
    # obter os nomes dos arquivos de configuracao e de saida da linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", type= str)#arquivo de configuração
    parser.add_argument("report_path", type= str)#arquivo de saida da linha de comando
    argumentos = parser.parse_args()
    
    # le o arquivo json e retorna como um dicionario
    config = load_config(argumentos.config_path)
    print(config['train_path'])

if __name__ == "__main__":
    main()