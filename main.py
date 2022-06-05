from libs import menu
from libs import stopwatch
from libs import history
from libs import open_task
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class WindowManager(ScreenManager):

    def __init__ (self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.menu = menu.Menu()
        self.stopwatch = stopwatch.Stopwatch()
        self.history = history.History()
        self.open_task = open_task.OpenTask()
        self.share()
        self.load()

    def load(self):
        screens = [self.menu, self.history, self.stopwatch, self.open_task]
        names = ['menu', 'history', 'stopwatch', 'open_task']
        for i in range(len(screens)):
            screen = screens[i]
            screen.name = names[i]
            self.add_widget(screen)

    def share(self):
        self.menu.start_task = self.menu_start_task
        self.stopwatch.back = self.stopwatch_back
        self.stopwatch.res_2 = self.stopwatch_res_2
        self.open_task.back_2 = self.open_task_back_2
        self.history.show_2 = self.history_show_2

    def menu_start_task(self, task):
        self.stopwatch.current_task = task
        self.stopwatch.ids.task_name.text = task.name.text
        self.current = 'stopwatch'

    def stopwatch_back(self):
        self.current = 'menu'

    def stopwatch_res_2(self, result):
        if result == 'Success':
            self.menu.delete_task(self.stopwatch.current_task)
        self.current = 'menu'

    def open_task_back_2(self):
        self.current = 'history'

    def history_show_2(self, tasks):
        self.open_task.tasks = tasks
        self.open_task.show()
        self.current = 'open_task'

    def other_button(self):
        if self.current == 'menu':
            self.current = 'history'
        else:
            self.current = 'menu'
                

wm = WindowManager()

wm.current = 'menu'

class TaskMaster(App):
    def build(self):
        return wm

if __name__ == '__main__':
    TaskMaster().run()
