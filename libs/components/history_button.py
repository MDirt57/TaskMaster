import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class HistoryButton(FloatLayout, Button):

    def __init__(self, **kwargs):
        super(HistoryButton, self).__init__(**kwargs)
        self.delete = Button(text = ':(', font_size = 36, size_hint = (.2, 1),\
                             pos_hint = {'x': .8, 'y': 0})
        self.name = Label(font_size = 36, pos_hint = {'x': 0, 'y': 0})
        self.add_widget(self.name)

    def edit(self):
        self.name.font_size = 18
        self.name.pos_hint = {'x': -.3, 'y': 0}
        self.add_widget(self.delete)

    def close_edit(self):
        self.remove_widget(self.delete)
        self.name.font_size = 36
        self.name.pos_hint = {'x': 0, 'y': 0}



class MyApp(App):
    def build(self):
        return HistoryButton()

if __name__ == '__main__':
    MyApp().run()
