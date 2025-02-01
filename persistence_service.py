import os
import pickle


class PersistenceService:
    def __init__(self, path: str):
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def store(self, key: str, data: object):
        with open(os.path.join(self.path, key), 'w') as file:
            pickle.dump(data, file)

    def retrieve(self, key: str):
        with open(os.path.join(self.path, key), 'r') as file:
            return pickle.load(file)
