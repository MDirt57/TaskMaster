import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from task_button import TaskButton
from ready import Ready

class Menu(Screen):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.tasks = []
        self.add_btn = Button(text = '+', font_size = 36, size_hint_y = None, height = self.height/2)
        self.add_btn.bind(on_press = self.add_task)
        self.edit_marker = 0
        self.ready_screen = Ready()
        self.ready_screen.size_hint = (.5, .5)
        self.ready_screen.pos_hint = {'x': .25, 'y': .25}
        self.ready_screen.no.bind(on_press = self.no)

    def edit(self):
        if self.edit_marker == 0:
            self.ids.task_list.add_widget(self.add_btn)
            if self.tasks != []:
                for i in self.tasks:
                    i.edit()
                    i.unbind(on_press = self.get_start)
            self.edit_marker = 1
        else:
            self.ids.task_list.remove_widget(self.add_btn)
            if self.tasks != []:
                for i in self.tasks:
                    i.close_edit()
                    i.bind(on_press = self.get_start)
                    try:
                        i.remove_widget(i.input)
                    except:
                        pass
            self.edit_marker = 0

    def add_task(self, instance):
        self.ids.task_list.remove_widget(self.add_btn)
        task = TaskButton()
        task.size_hint_y = None
        task.height = self.height/10
        self.tasks.append(task)
        task.delete.bind(on_press = lambda i: self.delete_task(task))
        self.ids.task_list.add_widget(task)
        self.ids.task_list.add_widget(self.add_btn)

    def delete_task(self, i):
        self.ids.task_list.remove_widget(i)
        del self.tasks[self.tasks.index(i)]

    def get_start(self, instance):
        self.add_widget(self.ready_screen)

    def no(self, instance):
        self.remove_widget(self.ready_screen)
        


kv = Builder.load_file('kv/menu.kv')

class TaskMaster(App):
    def build(self):
        return Menu()

if __name__ == '__main__':
    TaskMaster().run()
