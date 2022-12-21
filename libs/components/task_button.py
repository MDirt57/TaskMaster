from kivy.app import App
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivymd.uix.textfield import MDTextFieldRect
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class TaskButton(FloatLayout, MDRectangleFlatButton):

    def __init__(self, **kwargs):
        super(TaskButton, self).__init__(**kwargs)
        self.group = None
        self.current_time = '00:00:00'
        self.rename = True
        self.height = 100
        self.delete = MDIconButton(icon='delete', size_hint=(.1, 1), \
                                   pos_hint={'x': .9, 'y': 0})
        self.change_name = MDIconButton(icon='square-edit-outline', size_hint=(.1, 1), \
                                        pos_hint={'x': .8, 'y': 0})
        self.change_name.bind(on_release=self.change_name_)
        self.name = Label(font_size=self.width*.75, pos_hint={'x': 0, 'y': 0})
        self.input = MDTextFieldRect(multiline=False, font_size=self.width*.5, size_hint=(.6, .6), \
                                     background_color=(1, 1, 1, 1),
                                     foreground_color=(33 / 255, 150 / 255, 243 / 255, 1), \
                                     pos_hint={'top': .8, 'x': .2}, halign = "center")
        self.size_hint_x = 1
        self.input.bind(on_text_validate=self.set_name)
        self.add_widget(self.input)

    def set_name(self, instance):
        self.name.text = self.input.text
        self.add_widget(self.name)
        self.remove_widget(self.input)
        self.rename = False

    def set_name_(self, name):
        self.name.text = name
        self.add_widget(self.name)
        self.remove_widget(self.input)
        self.rename = False

    def edit(self):
        self.name.font_size = self.width*.045
        self.name.pos_hint = {'x': -.1, 'y': 0}
        self.add_widget(self.delete)
        self.add_widget(self.change_name)

    def change_name_(self, instance):
        if not self.rename:
            self.remove_widget(self.name)
            self.add_widget(self.input)
            self.input.text = self.name.text
            self.input.pos_hint = {'top': .8, 'x': .1}
            self.rename = True

    def close_edit(self):
        self.remove_widget(self.delete)
        self.remove_widget(self.change_name)
        self.name.font_size = self.width*.06
        self.name.pos_hint = {'x': 0, 'y': 0}

    def is_edit(self):
        return self.rename


class MyApp(App):
    def build(self):
        return TaskButton()


if __name__ == '__main__':
    MyApp().run()
