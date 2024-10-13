class Mode:

    def __init__(self, name: str, time_work: int, time_relax:int, time_long_relax:int):
        self.__name = name
        self.__time_work = time_work
        self.__time_relax = time_relax
        self.__time_long_relax = time_long_relax

    @property
    def time_work(self):
        return self.__time_work

    @time_work.setter
    def time_work(self, time):
        self.__time_work = time

    @property
    def time_relax(self):
        return self.__time_relax

    @time_relax.setter
    def time_relax(self, time):
        self.time_relax = time

    @property
    def time_long_relax(self):
        return self.__time_long_relax

    @time_long_relax.setter
    def time_long_relax(self, time):
        self.time_long_relax = time


class Timer:

    def __init__(self, time: int = 0, mode: Mode):
        self.__time = time
        self.__mode = mode
        self.__count_pomodoro = 0

    def start(self):
        pass

    def stop(self):
        pass

    def get_time(self):
        pass

    def set_time(self):
        pass

    def set_mode(self):
        pass

    def get_mode(self):
        pass

    def set_count(self):
        pass

    def get_count(self):
        pass


class Notification:

    def __init__(self, mode:Mode):
        self.__mode = mode

    def give_message(self):
        pass

    def set_mode(self):
        pass

    def get_mode(self):
        pass




class Statistic:

    def __init__(self, cycles, count_relax, count_work):
        self.__cycles = cycles
        self.__count_relax = count_relax
        self.__count_work = count_work

    @property
    def cycles(self):
        return self.__cycles

    @cycles.setter
    def cycles(self, value):
        self.__cycles = value

    @property
    def count_relax(self):
        return self.__count_relax

    @count_relax.setter
    def count_relax(self, value):
        self.__count_relax = value

    @property
    def count_work(self):
        return self.__count_work

    @count_work.setter
    def count_work(self, value):
        self.__count_work = value
