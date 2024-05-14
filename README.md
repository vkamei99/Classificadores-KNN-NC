<h1 align="center"> Teste de Classificadores (KNN, NC) </h1>

Este projeto consiste em criar um programa que permita comparar a performance de dois algoritmos de classificação (K-nearest neighbors, Nearest Centroid) em duas bases de dados diferentes: imagens (sem cores) e noticias (textos).

# Instalação
Para poder rodar o programa deve se instalar a biblioteca OpenCV e NunPy que pode ser instalada com os seguintes comandos:

Linux:

    sudo apt-get update
    sudo apt-get install python3-opencv
    sudo apt-get install python3-numpy

Windows:

    pip install opencv-python
    pip install numpy

para instalar a biblioteca, você precisa ter o Python e o pip (gerenciador de pacotes do Python) já instalados em seu sistema. Se você ainda não os tem, siga as instruções de instalação relevantes para o seu sistema operacional antes de prosseguir com a instalação das bibliotecas.

# Como Usar
## Entrada do programa

O programa deverá ser executado usando a linha de comando abaixo:


    python main.py data/configs/config.json data/reports/report.txt


na qual, config.json é um arquivo de configuração contendo informações de entrada para o programa e report.txt é o caminho do arquivo onde os dados de saída do experimento devem ser salvos. Segue abaixo como usá-los.

## Mudando o Dataset e o Algoritimo:

No diretório data/configs/ , existe um arquivo de configuração ja pronto. Você deve mudá-lo para testar o outro algoritmo ou o outro dataset segue abaixo como usá-lo de forma coerente com o codigo.

* O campo “type” indica o tipo do dataset que pode ser “image”(dataset de imagens) ou “news”(dataset de texto). 

* Os campos “train_path” e “test_path” contém o caminho para arquivos .txt que em cada linha contém o nome de um arquivo de imagem ou notícia e a respectiva classe (um exemplo é dado a seguir). *A mesma pasta contém pastas “train” e “test” nelas que estão armazenados os arquivos de imagens e notícias.* Mudando esses caminhos você deve passar o dataset novo ex: data/datasets/img_medium/train.txt

* O campo “classifier” indica qual classificador deve ser usado pelo programa (“knn” ou “nc”). 

### Exemplo do config.json
data/configs/config.json

    config.json
    {
        "type": "image",
        "train_path": "data/datasets/img_small/train.txt",
        "test_path": "data/datasets/img_small/test.txt",
        "classifier": "knn"
    }

[Config.json](https://github.com/vkamei99/Classificadores-KNN-NC/blob/main/data/configs/config.json)

### exemplo do train.txt:
data/reports/report

    train/c3719052006int.txt int
    train/3903082005int.txt int
    train/3829042006int.txt int
    train/a3426072006pot.txt pot
    train/3502072006pot.txt pot
    train/b1602062006poc.txt poc
    train/c1906052005poc.txt poc
    #estes são os nomes dos arquivos de noticia
 
[report](https://github.com/vkamei99/Classificadores-KNN-NC/blob/main/data/reports/report.txt)

## O arquivo de saída 

vai armazenar a acurácia do classificador, o tempo de treinamento por amostra e o tempo de predição por amostra . Um exemplo é dado abaixo:

    report.txt
    dataset: image
    path: data/datasets/news_small/
    classifier: knn
    training time per sample: 0.01s
    inference time per sample: 0.2s
    accuracy: 0.85

# Observações
* O projeto possui seu proprio sistema para vetorização de imagems e textos
* Para ajudar na organização do projeto foi usado um template dado pelo professor: Filipe Mutz

* No arquivo src/datasets/image_dataset.py no metodo get na linha 34 existe uma variavel "printar" se ela for True todas as imagens do dataset antes de serem vetorizadas vão aparecer na tela com o titulo do seu respectivo dataset

## Licença 

The [MIT License](https://github.com/vkamei99/Classificadores-KNN-NC/blob/main/LICENSE) (MIT)
