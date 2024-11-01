import json
import os

import modules.storage_low_buisness_logic as storage_lbl




class ServiceStorage:
    # должен создавать или загружать, а так же сохранять хранилище в файлы json или txt

    def __init__(self):
        # self.__storage = Storage()
        self.__expansion = 'json'
        self.__path = storage_lbl.take_path()

        if os.path.isfile(self.__path):
            self.__storage = self.load(self.__path, 'json')
        else:
            self.__storage = ServiceStorage.create(self, self.__path)




    def get_storage(self):
        return self.__storage


    def create(self, path):
        '''
        создаёт новое хранилище, создавая объект класса Storage и сохраняя его в json файл
        :return:
        '''
        storage = Storage()
        with open(path, "w") as write_file:
            json.dump(storage.toJson(), write_file)
        return storage


    def save(self, storage, path, expansion):
        '''
        сохраняет данные из 'storage' в файл с 'expansion'
        :param self:
        :param expansion:
        :return:
        '''
        if expansion == 'json':
            with open(path, "w") as write_file:
                json.dump(storage.toJson(), write_file)


    def load(self, path, expansion):
        if expansion == 'json':
            data = storage_lbl.json_load(path)
        elif expansion == 'txt':
            data = storage_lbl.txt_load(path)

        return data





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
