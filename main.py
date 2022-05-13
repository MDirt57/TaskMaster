import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



class Menu(Screen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.tasks = []
        self.add_btn = Button(text = '+', font_size = 36, size_hint_y = None, height = self.height/3)
        self.add_btn.bind(on_press = self.add_task)
        self.edit_marker = 0

    def edit(self):
        if self.edit_marker == 0:
            self.ids.task_list.add_widget(self.add_btn)
            self.edit_marker = 1
            for j in self.tasks:
                j[1].text += ' delete'
                j[1].bind(on_press = lambda j: self.delete_task(j))
        else:
            self.ids.task_list.remove_widget(self.add_btn)
            self.edit_marker = 0
            for j in self.tasks:
                j[1].text = '---'
                j[1].bind(on_press = self.op)

    def add_task(self, instance):
        self.ids.task_list.remove_widget(self.add_btn)
        task = Button(text = '---', font_size = 36, size_hint_y = None, height = self.height/10)
        name = task.text
        task.bind(on_press = lambda name: self.op(task.text))
        self.tasks.append((task.text, task))
        self.ids.task_list.add_widget(task)
        self.ids.task_list.add_widget(self.add_btn)

    def delete_task(self, btn):
        self.ids.task_list.remove_widget(btn)

    def op(self, name):
        print(name)

class History(Screen):
    pass

class Timer(Screen):
    pass

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
