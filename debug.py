from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.args import parse_args
import argparse
from src.io.config import load_config
from src.io.report import write_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", type= str)
    parser.add_argument("report_path", type= str)
    argumentos = parser.parse_args()
    
    config = load_config(argumentos.config_path)
    train_dataset = create_dataset(config["train_path"], config["type"])
    
    print(train_dataset.get(1))
    
if __name__ == "__main__":
    main()