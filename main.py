import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from threading import*
import time


class Menu(Screen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.tasks = {}
        self.add_btn = Button(text = '+', font_size = 36, size_hint_y = None, height = self.height/2)
        self.add_btn.bind(on_press = self.add_task)
        self.edit_marker = 0

    def edit(self):
        if self.edit_marker == 0:
            self.ids.task_list.add_widget(self.add_btn)
            self.edit_marker = 1
##            for j in self.tasks.values():
##                j.width = self.width/2
##                dell = Button(text = 'DEL', font_size = 36, size_hint_x = None, width = self.width/3)
##                self.ids.task_list.add_widget(dell)
        else:
            self.ids.task_list.remove_widget(self.add_btn)
            self.edit_marker = 0
            for j in self.tasks.values():
                j.bind(on_press = lambda j: self.get_start(j.text))


    def create_task(self, inp, name):
        self.tasks[inp].text = name
        self.ids.task_list.remove_widget(inp)

    def add_task(self, instance):
        self.ids.task_list.remove_widget(self.add_btn)
        task = Button(text = '', font_size = 36, size_hint_y = None, height = self.height/10)
        name = TextInput(multiline = False, size_hint_y = None, height = self.height/18)
        name.bind(on_text_validate = lambda name: self.create_task(name, name.text))
        self.ids.task_list.add_widget(name)
        self.tasks[name] = task
        self.ids.task_list.add_widget(task)
        self.ids.task_list.add_widget(self.add_btn)

    def delete_task(self, btn):
        self.ids.task_list.remove_widget(btn)
        print(self.tasks)

    def get_start(self, name):
        self.parent.get_screen('timer').ids.task_name.text = name
        self.parent.current = 'timer'

class History(Screen):
    pass

class Timer(Screen):

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)
        self.mstopwatch = 0
        self.t1 = Thread(target = self.seconds)
        self.iscounting = False

    def time_converter(self, seconds):
        current = self.ids.stopwatch.text
        sec = current[current.index(':') + 1:]
        print(sec)

    def start(self):
        if not self.iscounting:
            self.ids.start_pause.text = 'Pause'
            self.iscounting = True
            self.t1.start()
        
    def pause(self):
        self.iscounting = False
        self.t1.join()
        self.t1.do_run = False

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

    def seconds(self):
        diff = round(time.perf_counter())
        while self.iscounting:
            self.mstopwatch = round(time.perf_counter()) - diff
            self.ids.stopwatch.text = self.time_format(self.mstopwatch)


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('style.kv')
wm = WindowManager()

screens = [Menu(name = 'menu'), History(name = 'history'), Timer(name = 'timer')]
for screen in screens:
    wm.add_widget(screen)

wm.current = 'menu'

class TaskMaster(App):
    def build(self):
        return wm

if __name__ == '__main__':
    TaskMaster().run()
