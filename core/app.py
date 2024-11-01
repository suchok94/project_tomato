import json
import os
import configparser
import customtkinter
class App:

    def __init__(self, root):
        self.root = root





    #     config = configparser.ConfigParser()
    #     config.read('config.ini')
    #     path = config.get('Paths','storage_path')
    #
    #     if os.path.isfile(path):
    #         self.__storage = json.load()
    #     else:
    #         self.__storage = ServiceStorage.create(path)
    #
    # def get_storage(self):
    #     return self.__storage


class ServiceStorage:

    def __init__(self):
        pass
 # Нужен ли конструктор если все методы статичные?

    @staticmethod
    def create(path):
        '''
        создаёт новое хранилище, создавая объект класса Storage и сохраняя его в json файл
        :return:
        '''
        storage = Storage()
        with open(path, "w") as write_file:
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
        if expansion == 'json':
            with open("storage.json", "r") as read_file:
                data = read_file.read()
            return json.load(data)



class Storage:

    def __init__(self, statistic=1, list_modes=1):
        self.__statistic = statistic
        self.__list_modes = list_modes

    def get_statistic(self):
        return self.statistic

    def add_mode(self, mode):
        self.__list_modes.append(mode)

    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True, indent=4)
