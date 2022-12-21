from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

import sys, glob

sys.path.insert(0, 'libs/components/')
sys.path.append('../TaskMaster/res')
from task_button import TaskButton
from group_menu import GroupMenu

class Menu(MDScreen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.group_menu = GroupMenu()
        self.tasks = {}
        self.current_group = None
        self.groups = []
        self.add_btn = MDRectangleFlatButton(text='+', font_size=self.width*.48, md_bg_color=(0, 0, 0, 1), size_hint=(.2, .1))
        self.add_btn.bind(on_release=self.add_task)
        self.edit_marker = 0
        self.kv = Builder.load_file('libs/kv/main.kv')
        self.load()

    def edit(self):
        if self.edit_marker == 0:
            self.ids.edit.icon = 'window-close'
            self.ids.menu.add_widget(self.add_btn)
            if self.tasks[self.current_group] != []:
                for i in self.tasks[self.current_group]:
                    i.edit()
            self.edit_marker = 1
        else:
            self.ids.edit.icon = 'plus'
            self.ids.menu.remove_widget(self.add_btn)
            if self.tasks[self.current_group] != []:
                for i in self.tasks[self.current_group]:
                    i.close_edit()
                    if i.is_edit():
                        i.set_name_(i.input.text)
                    try:
                        i.remove_widget(i.input)
                    except:
                        pass
            self.edit_marker = 0

    def create_task(self, name = '', current_time = '00:00:00'):
        task = TaskButton()
        if name != '':
            task.set_name_(name)
            task.current_time = current_time
        task.size_hint_y = None
        task.group = self.current_group
        self.tasks[self.current_group].append(task)
        task.delete.bind(on_release=lambda i: self.delete_task(task))
        task.bind(on_release=lambda j: self.start_task(task))
        self.ids.task_list.add_widget(task)

    def load_one(self, group):
        self.tasks[group] = []
        with open(f'res/{group}.txt', 'r') as f:
            lines = f.read().splitlines()
        for line in lines:
            self.create_task(line[:-9], line[-8:])

    def load(self):
        groups = glob.glob('res/*.txt')
        for group in groups:
            name = group[4:-4]
            self.groups.append(name)
            self.current_group = name
            self.load_one(name)
        with open(f'../TaskMaster/cash.txt', 'r') as f:
            self.current_group = f.read()
        self.change_group(0)

    def add_task(self, instance):
        # self.ids.task_list.remove_widget(self.add_btn)
        self.create_task()
        # self.ids.task_list.add_widget(self.add_btn)

    def delete_task(self, task):
        self.ids.task_list.remove_widget(task)
        del self.tasks[self.current_group][self.tasks[self.current_group].index(task)]
        self.update()

    def delete_group(self, group):
        self.change_group(1)
        del self.tasks[group]
        self.groups.remove(group)


    def update(self):
        with open(f'../TaskMaster/cash.txt', 'w') as f:
            f.write(self.current_group)
        for name in self.groups:
            self.update_one(name)

    def update_one(self, name):
        with open(f'res/{name}.txt', 'w') as f:
            for task in self.tasks[name]:
                f.write(f'{task.name.text} {task.current_time}\n')

    def start_task(self, name):
        pass

    def change_group(self, vector): #vector = {-1, 1}
        self.update_one(self.current_group)
        try:
            self.current_group = self.groups[self.groups.index(self.current_group) + vector]
        except:
            self.current_group = self.groups[0]
        self.ids.group.text = self.current_group
        self.ids.task_list.clear_widgets()
        self.load_one(self.current_group)

    def add_group(self):
        self.ids.other.add_widget(self.group_menu)

kv = Builder.load_file('libs/kv/main.kv')

# class TaskMaster(MDApp):
#     def build(self):
#         return Menu()

# if __name__ == '__main__':
#     TaskMaster().run()
