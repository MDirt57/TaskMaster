import kivy
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

import sys
sys.path.insert(0, 'libs/components/')
from task_button import TaskButton

class Menu(MDScreen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.tasks = []
        self.add_btn = MDRectangleFlatButton(text = '+', font_size = 48, md_bg_color = (0, 0, 0, 1), size_hint = (.2, .1))
        self.add_btn.bind(on_press = self.add_task)
        self.edit_marker = 0
        self.kv = Builder.load_file('libs/kv/main.kv')
        self.load()

    def edit(self):
        if self.edit_marker == 0:
            self.ids.edit.icon = 'window-close'
            self.ids.menu.add_widget(self.add_btn)
            if self.tasks != []:
                for i in self.tasks:
                    i.edit()
            self.edit_marker = 1
        else:
            self.ids.edit.icon = 'plus'
            self.ids.menu.remove_widget(self.add_btn)
            if self.tasks != []:
                for i in self.tasks:
                    i.close_edit()
                    if i.is_edit():
                        i.set_name_(i.input.text)
                    try:
                        i.remove_widget(i.input)
                    except:
                        pass
            self.edit_marker = 0

    def create_task(self, name = ''):
        task = TaskButton()
        if name != '':
            task.set_name_(name)
        task.size_hint_y = None
        self.tasks.append(task)
        task.delete.bind(on_press = lambda i: self.delete_task(task))
        task.bind(on_press = lambda j: self.start_task(task))
        self.ids.task_list.add_widget(task)        

    def load(self):
        with open('libs/cash.txt', 'r') as f:
            lines = f.read().splitlines()
        for line in lines:
            self.create_task(line)
            
    def add_task(self, instance):
        # self.ids.task_list.remove_widget(self.add_btn)
        self.create_task()
        # self.ids.task_list.add_widget(self.add_btn)

    def delete_task(self, i):
        self.ids.task_list.remove_widget(i)
        del self.tasks[self.tasks.index(i)]
        self.update()

    def update(self):
        with open('libs/cash.txt', 'w') as f:
            for task in self.tasks:
                f.write(f'{task.name.text}\n')

    def start_task(self, name):
        pass

kv = Builder.load_file('libs/kv/main.kv')

# class TaskMaster(MDApp):
#     def build(self):
#         return Menu()

# if __name__ == '__main__':
#     TaskMaster().run()
