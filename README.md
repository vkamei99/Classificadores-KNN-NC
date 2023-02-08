# Teste de Classificadores
O trabalho consiste em criar um programa que permita comparar a performance de dois algoritmos de classificação (KNN, NC) em duas bases de dados diferentes: imagens(sem cores) e noticias(textos).

# Instalação
Para poder rodar deve se instalar a biblioteca OpenCV que pode ser instalada com o seguintes comandos:
Linux

    sudo apt-get update
    sudo apt-get install python3-opencv

Windows

    pip install opencv-python

para instalar a biblioteca, você precisa ter o Python e o pip (gerenciador de pacotes do Python) já instalados em seu sistema. Se você ainda não os tem, siga as instruções de instalação relevantes para o seu sistema operacional antes de prosseguir com a instalação da biblioteca OpenCV.

# Como Usar
O programa deverá ser executado usando a linha de comando abaixo:

    python main.py data/configs/config.json data/reports/report.txt

na qual, config.json é um arquivo de configuração contendo informações de entrada para o programa e report.txt é o caminho do arquivo onde os dados de saída do experimento devem ser salvos. No diretório data/configs, existe 1 arquivo de configuração ja pronto.

O arquivo config.json receberá como entrada um arquivo de configuração do tipo JSON como ilustrado abaixo. O campo “type” indica o tipo do dataset que pode ser “image” ou “news” (notícias). 
Os campos “train_path” e “test_path” contém o caminho para arquivos .txt que contém em cada linha o nome de um arquivo de imagem ou notícia e a respectiva classe. Um exemplo é dado a seguir. A mesma pasta que contém os arquivos train.txt e test.txt também contém pastas “train” e “test” e nelas estão armazenados os arquivos de imagens e notícias (veja, por exemplo, o diretório data/datasets/news-tiny). Por fim, o campo “classifier” indica qual classificador deve ser usado pelo programa (“knn” ou “nc”). 
Uma execução do programa consiste em avaliar um classificador específico em uma base de dados específica.

    config.json
    {
        "type": "image",
        "train_path": "data/datasets/img_small/train.txt",
        "test_path": "data/datasets/img_small/test.txt",
        "classifier": "knn"
    }

exemplo do train.txt:

    train.txt
    train/c3719052006int.txt int
    train/3903082005int.txt int
    train/3829042006int.txt int
    train/a3426072006pot.txt pot
    train/3502072006pot.txt pot
    train/b1602062006poc.txt poc
    train/c1906052005poc.txt poc
 
O arquivo de saída (report.txt no exemplo) deve armazenar a acurácia do classificador, o tempo de treinamento por amostra (tempo total de treino / número de amostras no treino) e o tempo de predição por amostra (tempo total de predição / número de amostras de teste). Um exemplo é dado abaixo:

    report.txt
    dataset: image
    path: data/datasets/news_small/
    classifier: knn
    training time per sample: 0.01s
    inference time per sample: 0.2s
    accuracy: 0.85

# Observações
* O projeto possui seu proprio sistema para vetorização de imagems e textos
* Foi usado um template dado pelo professor

# Autores
Este projeto foi feito por:
* Viktor Kamei Mota
* Arthur Christ Marcolan
* Enzo Dorigheto

