from libs import menu
from libs import stopwatch
from libs import history
from libs import open_task
import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from time import time
from kivy.lang import Builder
from kivy.core.window import Window

class WindowManager(ScreenManager):

    def __init__ (self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard = self.back)
        self.menu = menu.Menu()
        self.stopwatch = stopwatch.Stopwatch()
        self.history = history.History()
        self.open_task = open_task.OpenTask()
        self.share()
        self.load()
        self.set_view()

    def load(self):
        screens = [self.menu, self.history, self.stopwatch, self.open_task]
        names = ['menu', 'history', 'stopwatch', 'open_task']
        for i in range(len(screens)):
            screen = screens[i]
            screen.name = names[i]
            self.add_widget(screen)

    def share(self):
        self.menu.start_task = self.menu_start_task
        self.stopwatch.res_2 = self.stopwatch_res_2
        self.history.show_2 = self.history_show_2

    def menu_start_task(self, task):
        self.stopwatch.current_task = task
        self.stopwatch.ids.task_name.text = task.name.text
        self.current = 'stopwatch'

    def stopwatch_res_2(self, result):
        if result == 'Success':
            self.menu.delete_task(self.stopwatch.current_task)
        self.current = 'menu'

    def history_show_2(self, tasks):
        self.open_task.tasks = tasks
        self.open_task.show()
        self.current = 'open_task'

    def other_button(self):
        if self.current == 'menu':
            self.current = 'history'
            self.history.load()
        else:
            self.current = 'menu'

    def back(self, window, key, *largs):
        if key == 27:
            if self.current == 'stopwatch':
                self.current = 'menu'
                self.stopwatch.set_start()
            elif self.current == 'open_task':
                self.open_task.tasks = []
                self.open_task.ids.task_list.clear_widgets()
                self.current = 'history'
            return True
                
    def set_view(self):
        self.menu.ids.other.icon = 'history'
        self.menu.ids.edit.icon = 'plus'
        self.history.ids.other.icon = 'text-box-plus'
        self.history.ids.edit.icon = 'delete-outline'


class TaskMaster(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.wm = WindowManager()
        self.wm.current = 'menu'
        return self.wm

    def on_stop(self):
        self.wm.menu.update()

    def on_pause(self):
        self.wm.stopwatch.time_in_handling = time()
        return True

if __name__ == '__main__':
    TaskMaster().run()
