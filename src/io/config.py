from typing import Dict
import json

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    with open(path, 'r') as f:
        config_dict = json.load(f)
    #abre o arquivo json e o salva em "f" depois fecha o arquivo sozinho
    return config_dict

"""
Este código é uma função chamada load_config que lê um arquivo JSON e o retorna como um dicionário em Python.
A função recebe como parâmetro o caminho do arquivo (path: str) e retorna o dicionário (Dict).
O arquivo é aberto com o comando "with open (path, 'r') as f". Aqui, "f" é uma variável que será usada para referenciar o arquivo aberto.
Em seguida, usamos a função "json.load (f)" para ler o conteúdo do arquivo e armazená-lo como um dicionário em "config_dict".
Finalmente, a função retorna "config_dict" como resultado.
"""