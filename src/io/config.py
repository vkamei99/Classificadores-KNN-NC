from typing import Dict
import json

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    with open(path, 'r') as f:
        config_dict = json.load(f)
    #abre o arquivo json e o salva em "f" depois fecha o arquivo sozinho
    return config_dict
