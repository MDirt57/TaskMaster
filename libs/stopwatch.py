import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import date
from time import time

class Stopwatch(Screen):

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

    def set_start(self):
        self.ids.start_pause.text = 'Start'
        self.iscounting = False
        self.mstopwatch = 0
        self.ids.stopwatch.text = '00:00:00'
        

    def res(self, result):
        today = date.today()
        with open(f'libs/history/{today}.txt', 'a') as f:
            f.write(f'{self.ids.task_name.text}: {self.ids.stopwatch.text} | {result}!\n')
            f.close()
        self.set_start()
        self.res_2(result)

    def res_2(self, result):
        pass

    def back(self):
        pass


Builder.load_file('libs/kv/stopwatch.kv')

##class MyApp(App):
##    def build(self):
##        return Stopwatch()
##
##if __name__ == '__main__':
##    MyApp().run()
