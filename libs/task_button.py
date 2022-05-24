import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class TaskButton(FloatLayout, Button):

    def __init__(self, **kwargs):
        super(TaskButton, self).__init__(**kwargs)
        self.delete = Button(text = ':(', font_size = 36, size_hint = (.2, 1),\
                             pos_hint = {'x': .8, 'y': 0})
        self.change_name = Button(text = ';)', font_size = 36, size_hint = (.2, 1),\
                             pos_hint = {'x': .6, 'y': 0})
        self.change_name.bind(on_press = self.change_name_)
        self.name = Label(font_size = 36, pos_hint = {'x': 0, 'y': 0})
        self.input = TextInput(multiline = False, size_hint = (.6, .6),\
                              pos_hint = {'top': .8, 'x': .2})
        self.input.bind(on_text_validate = self.set_name)
        self.add_widget(self.input)
        self.background_down = self.background_normal

    def set_name(self, instance):
        self.name.text = self.input.text
        self.add_widget(self.name)
        self.remove_widget(self.input)

    def edit(self):
        self.name.font_size = 18
        self.name.pos_hint = {'x': -.3, 'y': 0}
        self.add_widget(self.delete)
        self.add_widget(self.change_name)

    def change_name_(self, instance):
        self.remove_widget(self.name)
        self.add_widget(self.input)
        self.input.pos_hint = {'x': .1, 'y': .25}
        self.input.size_hint = (.3, .6)

    def close_edit(self):
        self.remove_widget(self.delete)
        self.remove_widget(self.change_name)
        self.name.font_size = 36
        self.name.pos_hint = {'x': 0, 'y': 0}



class MyApp(App):
    def build(self):
        return TaskButton()

if __name__ == '__main__':
    MyApp().run()
