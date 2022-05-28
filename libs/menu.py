import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import sys
sys.path.insert(0, 'libs/components/')
from task_button import TaskButton

class Menu(Screen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.tasks = []
        self.add_btn = Button(text = '+', font_size = 36, size_hint_y = None, height = self.height/2)
        self.add_btn.bind(on_press = self.add_task)
        self.edit_marker = 0
##        self.load()

    def edit(self):
        if self.edit_marker == 0:
            self.ids.task_list.add_widget(self.add_btn)
            if self.tasks != []:
                for i in self.tasks:
                    i.edit()
            self.edit_marker = 1
        else:
            self.ids.task_list.remove_widget(self.add_btn)
            if self.tasks != []:
                for i in self.tasks:
                    i.close_edit()
                    try:
                        i.remove_widget(i.input)
                    except:
                        pass
            self.edit_marker = 0

    def create_task(self, name = '', size = 10):
        task = TaskButton()
        if name != '':
            task.set_name_(name)
        task.size_hint_y = None
        task.height = self.height/size
        self.tasks.append(task)
        task.delete.bind(on_press = lambda i: self.delete_task(task))
        task.bind(on_press = lambda j: self.start_task(task))
        self.ids.task_list.add_widget(task)        

##    def load(self):
##        with open('cash.txt', 'r') as f:
##            lines = f.read().splitlines()
##        for line in lines:
##            self.create_task(line, 1.75)
            
    def add_task(self, instance):
        self.ids.task_list.remove_widget(self.add_btn)
        self.create_task()
        self.ids.task_list.add_widget(self.add_btn)

    def delete_task(self, i):
        self.ids.task_list.remove_widget(i)
        del self.tasks[self.tasks.index(i)]

    def start_task(self, name):
        pass

kv = Builder.load_file('libs/kv/main.kv')

##class TaskMaster(App):
##    def build(self):
##        return Menu()
##
##if __name__ == '__main__':
##    TaskMaster().run()
