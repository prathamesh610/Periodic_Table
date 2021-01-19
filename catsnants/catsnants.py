#!/usr/bin /kivy
import kivy
from kivy.clock import Clock
from kivy.core.window import Window

kivy.require('1.7.2')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import webbrowser
from kivy.uix.videoplayer import VideoPlayer
import time

Window.fullscreen = 'auto'

Builder.load_file('ScreenManagement.kv')

Builder.load_file('LoadingScreen.kv')

Builder.load_file('gamepage1.kv')

Builder.load_file('gamepage2.kv')

Builder.load_file('exit_page.kv')


class LoadingScreen(Screen):
    pass


class screenOne(Screen):
    pass


class screenTwo(Screen):
    def on_enter(self, *args):
        self.score.text = self.manager.ids.screen1.ids.score.text


class exitPage(Screen):
    def on_enter(self, *args):
        if (self.manager.ids.screen2.ids.score.text == ""):
            self.exitPage_lable.text = self.manager.ids.screen1.ids.score.text
        else:
            self.exitPage_lable.text = self.manager.ids.screen2.ids.score.text


class ScreenManagement(ScreenManager):
    pass


# sm = ScreenManager()
#
# sm.add_widget(LoadingScreen(name="loading_screen"))
# sm.add_widget(screenOne(name="screen_one"))
# sm.add_widget(screenTwo(name="screen_two"))
# sm.add_widget(exitPage(name="exit_page"))


def get_id(instance):
    for id, widget in instance.parent.ids.items():
        if widget.__self__ == instance:
            return id


class MainApp(App):
    stack = []
    dict = {'Na': 'Cl', 'Ca': 'CO3', 'C': 'O2', 'N': 'H3', 'Ca': 'Cl2', 'Ba': 'O', 'K2': 'S', 'Cr2': 'O3'}
    list = ['NaCl', 'CaCO3', 'CO2', 'NH3', 'CaCl2', 'BaO', 'K2S', 'Cr2O3']
    counter = 0
    score = 0

    def Pressbtn(self, instance):

        global a, b, c
        self.stack.append(get_id(instance))
        if len(self.stack) == 2:
            a = (self.stack.pop(0))
            b = (self.stack.pop(0))
            # time.sleep(1)

            instance.parent.ids[b].background_color = (0.0, 0.0, 0.0, 1.0)
            instance.parent.ids[a].background_color = (0.0, 0.0, 0.0, 1.0)
            c = a + b
            self.counter = 1

        if self.counter == 1:
            self.counter = 0
            if c in self.list:
                self.score = self.score + 10
                instance.parent.ids[a].disabled = True
                instance.parent.ids[b].disabled = True
                instance.parent.ids.name.text = c
                instance.parent.ids.score.text = str(self.score)
            else:
                self.score -= 5
                if self.score >= 0:
                    instance.parent.ids.score.text = str(self.score)
                else:
                    self.score = 0
                    instance.parent.ids.score.text = str(self.score)

    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    MainApp().run()
