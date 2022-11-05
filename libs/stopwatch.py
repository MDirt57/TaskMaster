from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from datetime import date
from time import time

import sys

sys.path.append('TaskMaster/res')


class Stopwatch(MDScreen):

    def __init__(self, **kwargs):
        super(Stopwatch, self).__init__(**kwargs)
        self.mstopwatch = 0
        self.iscounting = False
        self.current_task = None
        self.time_in_handling = 0
        Clock.schedule_interval(self.second_counter, 1)

    def start_pause(self):
        if not self.iscounting:
            self.ids.start_pause.text = 'Pause'
            self.iscounting = True
        else:
            self.ids.start_pause.text = 'Start'
            self.iscounting = False

    def zeros_format(self, sec):
        if sec < 10:
            return f"0{sec}"
        return str(sec)

    def time_format(self, sec):
        if sec >= 60 and sec < 3600:
            return f"00:{self.zeros_format(sec // 60)}:{self.zeros_format(sec % 60)}"
        elif sec >= 3600:
            return f"{self.zeros_format(sec // 3600)}:{self.zeros_format(sec % 3600 // 60)}:{self.zeros_format(sec % 60)}"
        return f"00:00:{self.zeros_format(sec % 60)}"

    def second_counter(self, dt):
        if self.iscounting:
            if self.time_in_handling != 0:
                self.mstopwatch += round(time() - self.time_in_handling)
                self.time_in_handling = 0
            self.mstopwatch += 1
            self.ids.stopwatch.text = self.time_format(self.mstopwatch)
        else:
            self.time_in_handling = 0

    def sec_convert(self, time):
        time_list = time.split(':')
        seconds = int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])
        return seconds

    def set_time(self, name, time):
        self.ids.task_name.text = name
        self.ids.stopwatch.text = time
        self.mstopwatch = self.sec_convert(time)
        self.ids.start_pause.text = 'Start'
        self.iscounting = False

    def back(self):
        self.current_task.current_time = self.ids.stopwatch.text

    def res(self, result):
        with open(f'res/history/{self.current_task.group}.txt', 'a') as f:
            f.write(f'{self.ids.task_name.text}: {self.ids.stopwatch.text} | {result}!\n')
            f.close()
        self.back()
        self.res_2(result)

    def res_2(self, result):
        pass


Builder.load_file('libs/kv/stopwatch.kv')

##class MyApp(App):
##    def build(self):
##        return Stopwatch()
##
##if __name__ == '__main__':
##    MyApp().run()
