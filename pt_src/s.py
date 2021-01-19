#!/usr/bin/kivy
import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import webbrowser
from kivy.uix.videoplayer import VideoPlayer
import time

Builder.load_string('''
<MenuScreen>:
    GridLayout:
        padding: 5
        spacing: 5
        cols: 1
        padding: root.width*0.1
        Button:
            background_normal: ''
            background_color:(0.862, 0.078, 0.235, 0.9)
            text: 'PLAY'
            font_size: '20sp'
            on_press: root.manager.current='vdo'
            on_press: root.val1()
<Vdo>:
    GridLayout:
        cols: 1
        VideoPlayer:
            id: testid
            state: 'play'
            source: 'Video\Helium-Copy.webm'
            allow_stretch:'True'
            eos: 'loop'
            
            fullscreen: True
            # image_play: 'black.png'
            # image_stop: 'black.png'
            # image_pause: 'black.png'
            # image_volumehigh: 'black.png'
            # image_volumelow: 'black.png'
            # image_volumemedium: 'black.png'
            # image_volumemuted: 'black.png'
<Final>:
    GridLayout:
        cols: 1
        Label:
            text: 'over'

''')
# hdf
class MenuScreen(Screen):
    def val1(self):
        print ("1 is executed")
        vdo.ids.testid.state='play'
        sm.current='final'

class Vdo(Screen):
    def val2(self):
        print ("i am executed")

        def state_change(instance, value):
            if vdo.video.duration == vdo.video.position:
                sm.current = 'final'

        vdo.video.state.bind(state_change)

class Final(Screen):
    def val3(self):
        print ("i am executed")

sm = ScreenManager()
menu = MenuScreen(name='menu')
sm.add_widget(menu)
vdo = Vdo(name='vdo')
sm.add_widget(vdo)
final = Final(name='final')
sm.add_widget(final)

class MainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()


