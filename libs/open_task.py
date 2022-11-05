from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class OpenTask(MDScreen):

    def __init__(self, **kwargs):
        super(OpenTask, self).__init__(**kwargs)
        self.tasks = []

    def show(self):
        for task in self.tasks:
            t = Label(text=task, font_size=48, size_hint_y=None, height=50)
            if 'Success' in task:
                t.color = (0, 1, 0, 1)
            else:
                t.color = (1, 0, 0, 1)
            self.ids.task_list.add_widget(t)


kv = Builder.load_file('libs/kv/opentask.kv')

##class MyApp(App):
##    def build(self):
##        return OpenTask()
##
##if __name__ == '__main__':
##    MyApp().run()
