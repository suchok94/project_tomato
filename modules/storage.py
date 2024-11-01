import json
import os
import modules.timer
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
            self.create()

        # как лучше через просто метод или через присвоение результата?




    def get_storage(self):
        return self.__storage


    def create(self):
        '''
        создаёт новое хранилище, создавая объект класса Storage и сохраняя его в файл с расширением json или txt
        :return:
        '''
        self.__storage = Storage()
        if self.__expansion == 'json':
            storage_lbl.json_save(self.__storage, self.__path)

        elif self.__expansion == 'txt':
            storage_lbl.txt_save(self.__storage, self.__path)

        # может проверку убрать в нижнюю логику? передавая просто расширение файла


    def save(self):
        '''
        сохраняет данные из 'storage' в файл с 'expansion'
        :param self:
        '''
        if self.__expansion == 'json':
            storage_lbl.json_save(self.__storage, self.__path)

        elif self.__expansion == 'txt':
            storage_lbl.txt_save(self.__storage, self.__path)


    def load(self):
        if self.__expansion == 'json':
            data = storage_lbl.json_load(self.__path)
        elif self.__expansion == 'txt':
            data = storage_lbl.txt_load(self.__path)

        return data


    @property
    def expansion(self):
        return self.__expansion

    @expansion.setter
    def expansion(self, expansion):
        self.__expansion = expansion


class Storage:
    # само хранилище, которое хранит статистику и список модов для таймера
    # если создаётся с нуля, должно взять стандартный мод из конфига. статистику пустую(тоже из конфига?)

    def __init__(self, statistic=None, list_modes=None):
        if not(statistic is None):
            self.__statistic = statistic
        else:
            self.__statistic = modules.timer.Statistic(*storage_lbl.take_default_statistic())

        if not(list_modes is None):
            self.__list_modes = list_modes
        else:
            self.__list_modes = []
            self.__list_modes.append(modules.timer.Mode(*storage_lbl.take_standard_mode()))


    def get_statistic(self):
        return self.statistic

    def add_mode(self, mode):
        self.__list_modes.append(mode)

    def get_list_modes(self):
        return self.__list_modes

    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=True, indent=4)

    def toTxt(self):
        return 'заглушка'
