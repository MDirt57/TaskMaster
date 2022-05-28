import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class OpenTask(Screen):

    def __init__(self, **kwargs):
        super(OpenTask, self).__init__(**kwargs)
        self.tasks = []
        self.back = Button(text = '<-', font_size = 24, size_hint_y = None, height = self.height/3)         
        self.back.bind(on_press = self.back_)

    def show(self):
        for task in self.tasks:
            t = Label(text = task, font_size = 24, size_hint_y = None, height = 25)
            if 'Success' in task:
                t.color = (0,1,0,1)
            else:
                t.color = (1,0,0,1)
            self.ids.task_list.add_widget(t)
        self.ids.task_list.add_widget(self.back)

    def back_(self, instance):
        self.tasks = []
        self.ids.task_list.clear_widgets()
        self.back_2()

    def back_2(self):
        pass

kv = Builder.load_file('libs/kv/opentask.kv')

##class MyApp(App):
##    def build(self):
##        return OpenTask()
##
##if __name__ == '__main__':
##    MyApp().run()
