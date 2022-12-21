from libs import menu
from libs import stopwatch
from libs import history
from libs import open_task
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from time import time
from kivy.core.window import Window


class WindowManager(ScreenManager):

    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.back)
        self.menu = menu.Menu()
        self.stopwatch = stopwatch.Stopwatch()
        self.history = history.History()
        self.open_task = open_task.OpenTask()
        self.share()
        self.load()
        self.set_view()
        self.is_touch = False

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
        self.stopwatch.set_time(task.name.text, task.current_time)
        self.current = 'stopwatch'

    def stopwatch_res_2(self):
        self.menu.delete_task(self.stopwatch.current_task)
        self.menu.update()
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
                self.stopwatch.back()
                self.current = 'menu'
            elif self.current == 'open_task':
                self.open_task.tasks = []
                self.open_task.ids.task_list.clear_widgets()
                self.current = 'history'
            return True

    def set_view(self):
        self.menu.ids.other.icon = 'clipboard-plus-outline'
        self.menu.ids.edit.icon = 'plus'
        self.history.ids.other.icon = 'text-box-plus'
        self.history.ids.edit.icon = 'delete-outline'


    def on_touch_move(self, touch):
        if touch.y > 540 and touch.y < 600:
            if not self.is_touch:
                if touch.x > 200 and touch.x < 600 and touch.x - touch.ox > 200:
                    self.menu.change_group(-1)
                    self.is_touch = True
                elif touch.x > 200 and touch.x < 600 and touch.ox - touch.x > 200:
                    self.menu.change_group(1)
                    self.is_touch = True
        else:
            if touch.x - touch.ox > 200 and self.current == 'menu':
                self.transition.direction = 'right'
                self.current = 'history'
                self.history.load()
            elif touch.ox - touch.x > 200 and self.current == 'history':
                self.transition.direction = 'left'
                self.current = 'menu'

    def on_touch_up(self, touch):
        self.is_touch = False

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
