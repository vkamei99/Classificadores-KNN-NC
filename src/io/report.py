
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    arquivo = open(path, 'w')
    arquivo.write(metrics_values)

