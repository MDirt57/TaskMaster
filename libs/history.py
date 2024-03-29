from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
import os
import glob

import sys

sys.path.insert(0, 'libs/components/')
from history_button import HistoryButton

sys.path.append('TaskMaster/res')


class History(MDScreen):

    def __init__(self, **kwargs):
        super(History, self).__init__(**kwargs)
        self.ids.group.add_widget(Label(text='History', font_size=48))
        self.directory = 'res/history'
        self.tasks = []
        self.edit_marker = 0
        self.results = []
        self.files_ = []

    def edit(self):
        if self.edit_marker == 0:
            self.ids.edit.icon = 'delete-off-outline'
            if self.tasks != []:
                for i in self.tasks:
                    i.edit()
            self.edit_marker = 1
        else:
            self.ids.edit.icon = 'delete-outline'
            if self.tasks != []:
                for i in self.tasks:
                    i.close_edit()
            self.edit_marker = 0

    def load_(self, filename):
        if filename not in self.files_:
            self.files_.append(filename)
            task = HistoryButton()
            task.size_hint_y = None
            task.name.text = filename[12:-4]
            task.path = filename
            task.delete.bind(on_release=lambda i: self.delete_task(task))
            task.bind(on_release=lambda j: self.show(filename))
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
        self.files_.remove(i.path)
        del self.tasks[self.tasks.index(i)]
        os.remove(i.path)

    def add_group(self):
        pass
