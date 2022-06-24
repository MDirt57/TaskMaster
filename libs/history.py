import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os
import glob

import sys
sys.path.insert(0, 'libs/components/')
from history_button import HistoryButton

class History(Screen):

    def __init__(self, **kwargs):
        super(History, self).__init__(**kwargs)
        self.directory = 'libs/history'
        self.tasks = []
        self.edit_marker = 0
        self.results = []
        self.files_ = []

    def edit(self):
        if self.edit_marker == 0:
            if self.tasks != []:
                for i in self.tasks:
                    i.edit()
            self.edit_marker = 1
        else:
            if self.tasks != []:
                for i in self.tasks:
                    i.close_edit()
            self.edit_marker = 0
    
    def load_(self, filename):
        if filename not in self.files_:
            self.files_.append(filename)
            task = HistoryButton()
            task.size_hint_y = None
            task.height = 50
            task.name.text = filename[13:]
            task.path = filename
            task.delete.bind(on_press = lambda i: self.delete_task(task))
            task.bind(on_press = lambda j: self.show(filename))
            self.ids.task_list.add_widget(task)
            self.tasks.append(task)

    def load(self):
        for filename in glob.glob(glob.escape(self.directory) + '/*.txt'):
            self.load_(filename)

    def show(self, file):
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for task in lines:
                self.results.append(task)
        self.show_2(self.results)
        self.results = []

    def show_2(self, tasks):
        pass

    def delete_task(self, i):
        self.ids.task_list.remove_widget(i)
        del self.tasks[self.tasks.index(i)]
        os.remove(i.path)



kv = Builder.load_file('libs/kv/main.kv')

##class MyApp(App):
##    def build(self):
##        return History()
##
##if __name__ == '__main__':
##    MyApp().run()
