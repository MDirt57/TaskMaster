from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

Builder.load_string(
    '''
<GroupMenu>

    GridLayout:
    
        rows: 3
        MDRectangleFlatIconButton:
            id: add
            icon: 'plus'
            size_hint: 1/8, 1
            text: 'add group'
            on_press: root.add()
            
        MDRectangleFlatIconButton:
            id: edit
            icon: 'square-edit-outline'
            size_hint: 1/8, 1
            text: 'edit name'
            on_press: root.edit()
            
        MDRectangleFlatIconButton:
            id: delete
            icon: 'delete-outline'
            size_hint: 1/8, 1
            text: 'delete'
            on_press: root.delete()
    '''
)

class GroupMenu(Widget):

    def __init__(self, **kwargs):
        super(GroupMenu, self).__init__(**kwargs)
        self.size_hint_x = .1

    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

class MyApp(MDApp):
    def build(self):
        return GroupMenu()

if __name__ == '__main__':
    MyApp().run()