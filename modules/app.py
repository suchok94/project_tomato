import json
import configparser
class App:

    def __init__(self, root, storage=None):
        self.root = root

        if storage is None:
            self.__storage = ServiceStorage.create()


class ServiceStorage:

    def __init__(self):
        pass

    @staticmethod
    def create():
        '''
        создаёт новое хранилище, создавая объект класса Storage и сохраняя его в json файл
        :return:
        '''
        storage = Storage()
        with open("storage.json", "w") as write_file:
            json.dump(storage.toJson(), write_file)
        return storage

    @staticmethod
    def save(storage, expansion):
        '''
        сохраняет данные из 'storage' в файл с 'expansion'
        :param self:
        :param expansion:
        :return:
        '''
        if expansion == 'json':
            with open("storage.json", "w") as write_file:
                json.dump(storage.toJson(), write_file)

    @staticmethod
    def load(expansion):
        pass


class Storage:

    def __init__(self, statistic= None, list_modes=None):
        self.statistic = statistic
        self.list_modes = list_modes

    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True, indent=4)
