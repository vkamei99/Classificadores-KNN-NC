
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    #criar gabarito (true_classes)
    #comparar gabarito com o treino (predicted_classes)
    quantidade = 0 #quantidade de vetores usados no treino
    acertos = 0

    for i in range(quantidade):
        if true_classes[i] == predicted_classes[i]:
            acertos += 1
    
    acurracy = (acertos*100)/quantidade

    return accuracy
