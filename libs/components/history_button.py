import kivy
from kivy.app import App
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class HistoryButton(FloatLayout, MDRectangleFlatButton):

    def __init__(self, **kwargs):
        super(HistoryButton, self).__init__(**kwargs)
        self.height = 100
        self.delete = MDIconButton(icon = 'delete', font_size = 36, size_hint = (.1, 1),\
                             pos_hint = {'x': .9, 'y': 0})
        self.name = Label(font_size = 48, pos_hint = {'x': 0, 'y': 0})
        self.size_hint_x = 1
        self.add_widget(self.name)
        self.path = None
        
    def edit(self):
        self.name.font_size = 36
        self.name.pos_hint = {'x': -.3, 'y': 0}
        self.add_widget(self.delete)

    def close_edit(self):
        self.remove_widget(self.delete)
        self.name.font_size = 48
        self.name.pos_hint = {'x': 0, 'y': 0}



# class MyApp(App):
#     def build(self):
#         return HistoryButton()

# if __name__ == '__main__':
#     MyApp().run()
