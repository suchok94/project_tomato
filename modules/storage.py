import json
import os

import modules.storage_low_buisness_logic as storage_lbl




class ServiceStorage:
    # должен создавать или загружать, а так же сохранять хранилище в файлы json или txt

    def __init__(self):
        # self.__storage = Storage()
        self.__expansion = 'json'
        self.__path = storage_lbl.take_path(self.__expansion)

        if os.path.isfile(self.__path):
            self.__storage = self.load()
        else:
            self.__storage = ServiceStorage.create(self)




    def get_storage(self):
        return self.__storage


    def create(self):
        '''
        создаёт новое хранилище, создавая объект класса Storage и сохраняя его в json файл
        :return:
        '''
        storage = Storage()
        if self.__expansion == 'json':
            storage_lbl.json_save(storage, self.__path)

        elif self.__expansion == 'txt':
            storage_lbl.txt_save(storage, self.__path)

        return storage


    def save(self):
        '''
        сохраняет данные из 'storage' в файл с 'expansion'
        :param self:
        :param expansion:
        :return:
        '''
        if self.__expansion == 'json':
            storage_lbl.json_save(self.__storage, self.__path)

        elif self.__expansion == 'txt':
            storage_lbl.txt_save(self.__storage, self.__path)


    def load(self, path, expansion):
        if expansion == 'json':
            data = storage_lbl.json_load(path)
        elif expansion == 'txt':
            data = storage_lbl.txt_load(path)

        return data


    @property
    def expansion(self):
        return self.__expansion

    @expansion.setter
    def expansion(self, expansion):
        self.__expansion = expansion


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

    def toTxt(self):
        return 'заглушка'
