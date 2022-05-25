import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import date

class Stopwatch(Screen):

    def __init__(self, **kwargs):
        super(Stopwatch, self).__init__(**kwargs)
        self.mstopwatch = 0
        self.iscounting = False

    def start_pause(self):
        if not self.iscounting:
            self.ids.start_pause.text = 'Pause'
            self.iscounting = True
            Clock.schedule_interval(self.second_counter, 1)
        else:
            self.ids.start_pause.text = 'Start'
            self.iscounting = False

    def zeros_format(self, sec):
        if sec < 10:
            return f"0{sec}"
        return str(sec)

    def time_format(self, sec):
        if sec > 60 and sec < 3600:
            return f"00:{self.zeros_format(sec // 60)}:{self.zeros_format(sec % 60)}"
        elif sec > 3600:
            return f"{self.zeros_format(sec // 3600)}:{self.zeros_format(sec % 3600 // 60)}:{self.zeros_format(sec % 60)}"
        return f"00:00:{self.zeros_format(sec % 60)}"

    def second_counter(self, dt):
        if self.iscounting:
            self.mstopwatch += 1
            self.ids.stopwatch.text = self.time_format(self.mstopwatch)

    def res(self, result):
        today = date.today()
        with open(f'{today}.txt', 'a') as f:
            f.write(f'{self.ids.task_name.text}: {self.ids.stopwatch.text} | {result}!\n')
            f.close()


Builder.load_file('kv/stopwatch.kv')

class MyApp(App):
    def build(self):
        return Stopwatch()

if __name__ == '__main__':
    MyApp().run()
