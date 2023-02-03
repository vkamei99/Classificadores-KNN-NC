dicionario = {"chave":"valor"}

dummy_dict = {
        "train_dataset": {
            "type": "image",
            "path": "data/datasets/img_small/train.txt"
        },
        "test_dataset": {
            "type": "image",
            "path": "data/datasets/img_small/test.txt"
        },
        "classifier": {
            "type": "knn"
        }
    }

print(dummy_dict["train_dataset"]['path'])