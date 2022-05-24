import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class Ready(FloatLayout):

    def __init__(self, **kwargs):
        super(Ready, self).__init__(**kwargs)
        self.backgr = Button(background_color = (0,1,0,1), size_hint = (1, 1), pos_hint = {'x': 0, 'y': 0})
        self.backgr.disabled = True
        self.label = Label(text = 'Ready?', color = (1,1,1,1), font_size = 36, pos_hint = {'x': 0, 'y': .3})
        self.no = Button(text = 'No', font_size = 36, size_hint = (.3, .3),\
                         pos_hint = {'x': .1, 'y': .2})
        self.yes = Button(text = 'Yes', font_size = 36, size_hint = (.3, .3),\
                         pos_hint = {'x': .6, 'y': .2})
        self.add_widget(self.backgr)
        self.add_widget(self.label)
        self.add_widget(self.no)
        self.add_widget(self.yes)
        


class MyApp(App):
    def build(self):
        return Ready()

if __name__ == '__main__':
    MyApp().run()
