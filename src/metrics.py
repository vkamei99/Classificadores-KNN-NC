
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    quantidade = len(true_classes) #quantidade de vetores usados no treino
    acertos = 0

    for i in range(quantidade):
        if true_classes[i] == predicted_classes[i]:
            acertos += 1
    
    porcentagem = (acertos)/quantidade

    return porcentagem
