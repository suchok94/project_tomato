import time

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

    def __init__(self, mode: Mode, time: int = 0):
        self.__time = time
        self.__mode = mode
        self.__count_pomodoro = 0.0

    def check_phase(self):
        phase = self.__mode.time_work
        phase_id = 0

        if self.__count_pomodoro != 0 and self.__count_pomodoro % 4 == 0:
            phase = self.__mode.time_long_relax
            phase_id = 2

        elif self.__count_pomodoro % 1 != 0:
            phase = self.__mode.time_relax
            phase_id = 1

        return phase, phase_id

    def start(self):
        phase = self.check_phase()

        self.__time = phase[0]
        while self.__time:
            time.sleep(1)
            self.__time -= 1
            # выдаёт время на табло


        # выдаёт уведомление о окончании таймера
        notification = Notification(phase[1])
        notification.give_message()

        self.__count_pomodoro += 0.5

        self.start()

    # мусор
    # def start_work(self):
    #
    #     self.__time = self.__mode.time_work
    #
    #     while self.__time:
    #         time.sleep(1)
    #         self.__time -= 1
    #         print(self.__time)
    #
    #
    #
    #
    #
    # def start_relax(self):
    #     self.__time = self.__mode.time_relax
    #
    #     while self.__time:
    #         time.sleep(1)
    #         self.__time -= 1
    #         print(self.__time)
    #
    #     self.__count_pomodoro += 1
    #
    # def start_long_relax(self):
    #     self.__time = self.__mode.time_long_relax
    #     while self.__time:
    #         time.sleep(1)
    #         self.__time -= 1
    #         print(self.__time)


    def stop(self):
        self.__time = 0

    #??
    # def pause(self):
    #     pass

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode

    @property
    def count(self):
        return self.__count_pomodoro

    @count.setter
    def set_count(self, count):
        self.__count_pomodoro = count




class Notification:
    # должен принимать id режима Mode и выдавать соответствующее уведомление

    def __init__(self, phase_id: int):
        self.__phase_id = phase_id

    def give_message(self):
        if self.__phase_id == 0:
            pass # вывод сообщения что работа закончена
        elif self.__phase_id == 1:
            pass # вывод сообщения что отдых закончен
        else:
            pass # вывод сообщения что длинный отдых закончен




    @property
    def phase_id(self):
        return self.__phase_id

    @phase_id.setter
    def phase_id(self, phase_id):
        self.__phase_id = phase_id


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
