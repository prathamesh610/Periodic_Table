import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import time
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import FadeTransition
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.uix.progressbar import ProgressBar
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

Window.fullscreen = 'auto'
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
Window.fullscreen = 'auto'

# Window.clearcolor = (1, 1, 1, 1)
# You can create your kv code in the Python file
Builder.load_string("""
<ScreenOne>:
    on_enter:
        screenone_video.state='play'
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'center'
        Video:
            id: screenone_video
            fullscreen:True
            # state: 'play'
            source: r'Video/sssolving_the_puzzle_of_the_periodic.mp4'
            allow_stretch:'True'
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Skip"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.ids.screenone_video.state = 'stop'
                root.manager.current = 'intro_screen'
<IntroScreen>:
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: r'cover/My Post (2).png'
    # AnchorLayout:
    #     anchor_x : 'right'
    #     anchor_y : 'bottom'
    #     Button:
    #         # background_normal: 'cover/My Post (1).png'
    #         size_hint: .1,.1          #button size
    #         size: .5,.5
    #         text: "-->"
    #         pos_hint:{"center_x":1,"center_y":0.1}
    #
    #         on_press:
    #             # You can define the duration of the change
    #             # and the direction of the slide
    #             root.manager.transition.direction = 'left'
    #             root.manager.transition.duration = 0
    #             root.manager.current = 'screen_two'
    FloatLayout:
        Button:
            size_hint: .2,.1
            size: 15,5
            # text: "Start"
            pos_hint:{"center_x":0.5,"center_y":0.3}
            background_normal: 'cover/My Post (1).png'
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<Electro>
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: r'elements_images/Periodic_Table_of_Elements_w_Electronegativity_PubChem.png'
    Button:
        size_hint: .1,.05
        size: 15,5
        text: "Back"
        pos_hint:{"left":1,"bottom":0}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0
            root.manager.current = 'screen_two'
<Oxidation>
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: r'elements_images/Periodic_Table_of_Elements_w_Oxidation_States_PubChem.png'
    Button:
        size_hint: .1,.05
        size: 15,5
        text: "Back"
        pos_hint:{"left":1,"bottom":0}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0
            root.manager.current = 'screen_two'
<StdState>
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: r'elements_images/Periodic_Table_of_Elements_w_Standard_State_PubChem.png'
    Button:
        size_hint: .1,.05
        size: 15,5
        text: "Back"
        pos_hint:{"left":1,"bottom":0}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0
            root.manager.current = 'screen_two'
<ScreenTwo>:
    GridLayout:
        cols: 19
        rows: 11
        Label:
            text: "[color=000000][size=32]P/G[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]1[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]2[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]3[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]4[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]5[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]6[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]7[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]8[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]9[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]10[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]11[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]12[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]13[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]14[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]15[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]16[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]17[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]18[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "[color=000000][size=32]1[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############  HYDROGEN ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_three'
            Image:
                source: r'elements_images/H.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "22"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "23"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "24"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "25"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "26"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "27"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "28"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "29"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "30"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "31"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "32"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "33"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "34"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "35"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "36"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ########## HELIUM #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_four'
            Image:
                source: r'elements_images/He.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "[color=000000][size=32]2[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ########### LITHIUM #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_five'
            Image:
                source: r'elements_images/Li.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ######### BERYLLIUM #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_six'
            Image:
                source: r'elements_images/Be.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "42"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "43"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "44"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "45"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "46"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "47"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "48"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "49"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "50"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "51"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ########## BORON ########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seven'
            Image:
                source: r'elements_images/B.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ######### CARBON ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eight'
            Image:
                source: r'elements_images/C.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############### NITRROGEN ###########33
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_nine'
            Image:
                source: r'elements_images/N.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### OXYGEN ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ten'
            Image:
                source: r'elements_images/O.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### FLUORINE ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eleven'
            Image:
                source: r'elements_images/F.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############# NEON ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twelve'
            Image:
                source: r'elements_images/Ne.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "[color=000000][size=32]3[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############# SODIUM ###############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirteen'
            Image:
                source: r'elements_images/Na.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############## MAGNESIUM ###############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourteen'
            Image:
                source: r'elements_images/Mg.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "61"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "62"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "63"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "64"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "65"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "66"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "67"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "68"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "69"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "70"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############ ALUMINIUM #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fifteen'
            Image:
                source: r'elements_images/Al.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### SILICON ##################
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixteen'
            Image:
                source: r'elements_images/Si.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            #### PHOSPHOROUS ###########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventeen'
            Image:
                source: r'elements_images/P.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
        ########## SULPHHUR ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eighteen'
            Image:
                source: r'elements_images/S.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ##### CHLORINE #########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_nineteen'
            Image:
                source: r'elements_images/Cl.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## ARGON ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twenty'
            Image:
                source: r'elements_images/Ar.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "[color=000000][size=32]4[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ######## POTASSIUM ###########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentyone'
            Image:
                source: r'elements_images/K.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ CALCIUM ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentytwo'
            Image:
                source: r'elements_images/Ca.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################## SCANDIUM ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentythree'
            Image:
                source: r'elements_images/Sc.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ti ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentyfour'
            Image:
                source: r'elements_images/Ti.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## V #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentyfive'
            Image:
                source: r'elements_images/V.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############## Cr ##################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentysix'
            Image:
                source: r'elements_images/Cr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## Mn ################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentyseven'
            Image:
                source: r'elements_images/Mn.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############# Fe #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentyeight'
            Image:
                source: r'elements_images/Fe.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## Co #########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_twentynine'
            Image:
                source: r'elements_images/Co.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### Ni #################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirty'
            Image:
                source: r'elements_images/Ni.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## Cu #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtyone'
            Image:
                source: r'elements_images/Cu.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## Zn ##########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtytwo'
            Image:
                source: r'elements_images/Zn.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################ Ga #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtythree'
            Image:
                source: r'elements_images/Ga.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################ Ge ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtyfour'
            Image:
                source: r'elements_images/Ge.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############# As ##############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtyfive'
            Image:
                source: r'elements_images/As.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### Se #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtysix'
            Image:
                source: r'elements_images/Se.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############### Br ##########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtyseven'
            Image:
                source: r'elements_images/Br.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############### Kr ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtyeight'
            Image:
                source: r'elements_images/Kr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "[color=000000][size=32]5[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############### Rb ##########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_thirtynine'
            Image:
                source: r'elements_images/Rb.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### Sr ########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourty'
            Image:
                source: r'elements_images/Sr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########### Y ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtyone'
            Image:
                source: r'elements_images/Y.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############# Zr ##################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtytwo'
            Image:
                source: r'elements_images/Zr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################ Nb ################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtythree'
            Image:
                source: r'elements_images/Nb.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############# Mo #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtyfour'
            Image:
                source: r'elements_images/Mo.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############## Tc ################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtyfive'
            Image:
                source: r'elements_images/Tc.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ru ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtysix'
            Image:
                source: r'elements_images/Ru.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################ Rh ################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtyseven'
            Image:
                source: r'elements_images/Rh.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############# Pd ###############
            Image:
                source: r'elements_images/Pd.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ########## Ag ##################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fourtynine'
            Image:
                source: r'elements_images/Ag.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############### Cd ################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fifty'
            Image:
                source: r'elements_images/Cd.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################## In ###############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftyone'
            Image:
                source: r'elements_images/In.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################# Sn #######################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftytwo'
            Image:
                source: r'elements_images/Sn.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################## Sb ################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftythree'
            Image:
                source: r'elements_images/Sb.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
             ############### Te ###############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftyfour'
            Image:
                source: r'elements_images/Te.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############### I ############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftyfive'
            Image:
                source: r'elements_images/I.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ################## Xe ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftysix'
            Image:
                source: r'elements_images/Xe.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "[color=000000][size=32]6[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############# Cs ###########
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftyseven'
            Image:
                source: r'elements_images/Cs.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
             ##################### Ba #############
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftyeight'
            Image:
                source: r'elements_images/Ba.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: '[color=000000]     [size=12]series[/size]\\n[size=38][b]*La[/color][/size][/b]'
            markup:True
            background_normal: ''
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: .9098039,.6528823,.32941,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############ Hf ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_fiftynine'
            Image:
                source: r'elements_images/Hf.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ta ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixty'
            Image:
                source: r'elements_images/Ta.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ W ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtyone'
            Image:
                source: r'elements_images/W.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Re ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtytwo'
            Image:
                source: r'elements_images/Re.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Os ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtythree'
            Image:
                source: r'elements_images/Os.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ir ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtyfour'
            Image:
                source: r'elements_images/Ir.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Pt ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtyfive'
            Image:
                source: r'elements_images/Pt.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Au ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtysix'
            Image:
                source: r'elements_images/Au.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Hg ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtyseven'
            Image:
                source: r'elements_images/Hg.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Tl ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtyeight'
            Image:
                source: r'elements_images/Tl.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Pb ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_sixtynine'
            Image:
                source: r'elements_images/Pb.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Bi ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventy'
            Image:
                source: r'elements_images/Bi.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Po ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventyone'
            Image:
                source: r'elements_images/Po.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ At ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventytwo'
            Image:
                source: r'elements_images/At.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Rn ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventythree'
            Image:
                source: r'elements_images/Rn.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "[color=000000][size=32]7[/color][/size]"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############ Fr ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventyfour'
            Image:
                source: r'elements_images/Fr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ra ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventyfive'
            Image:
                source: r'elements_images/Ra.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ac ###################
            text: '[color=000000]     [size=12]series[/size]\\n[size=38][b]*Ac[/color][/size][/b]'
            markup:True
            background_normal: ''
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: .01568627,.2666666666,.7647,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############ Rf ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventysix'
            Image:
                source: r'elements_images/Rf.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Db ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventyseven'
            Image:
                source: r'elements_images/Db.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Sg ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventyeight'
            Image:
                source: r'elements_images/Sg.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Bh ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_seventynine'
            Image:
                source: r'elements_images/Bh.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Hs ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eighty'
            Image:
                source: r'elements_images/Hs.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Mt ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightyone'
            Image:
                source: r'elements_images/Mt.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ds ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightytwo'
            Image:
                source: r'elements_images/Ds.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Rg ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightythree'
            Image:
                source: r'elements_images/Rg.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Cn ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightyfour'
            Image:
                source: r'elements_images/Cn.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Nh ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightyfive'
            Image:
                source: r'elements_images/Nh.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Fl ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightysix'
            Image:
                source: r'elements_images/Fl.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Mc ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightyseven'
            Image:
                source: r'elements_images/Mc.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Lv ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightyeight'
            Image:
                source: r'elements_images/Lv.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ts ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_eightynine'
            Image:
                source: r'elements_images/Ts.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Og ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninety'
            Image:
                source: r'elements_images/Og.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "153"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "154"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "155"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "156"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "157"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "158"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "159"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "160"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "161"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "162"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "163"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "164"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "165"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "166"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "167"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "168"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "169"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "170"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "171"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: "172"
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: '[color=000000]     [size=12]series[/size]\\n[size=38][b]*La[/color][/size][/b]'
            markup:True
            background_normal: ''
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: .9098039,.6528823,.32941,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############ La ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetyone'
            Image:
                source: r'elements_images/La.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ce ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetythree'
            Image:
                source: r'elements_images/Ce.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Pr ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetyfour'
            Image:
                source: r'elements_images/Pr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Nd ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetyfive'
            Image:
                source: r'elements_images/Nd.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Pm ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetysix'
            Image:
                source: r'elements_images/Pm.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Sm ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetyseven'
            Image:
                source: r'elements_images/Sm.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Eu ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetyeight'
            Image:
                source: r'elements_images/Eu.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Gd ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetynine'
            Image:
                source: r'elements_images/Gd.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Tb ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundred'
            Image:
                source: r'elements_images/Tb.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Dy ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredone'
            Image:
                source: r'elements_images/Dy.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Ho ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredtwo'
            Image:
                source: r'elements_images/Ho.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Er ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredthree'
            Image:
                source: r'elements_images/Er.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Tm ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredfour'
            Image:
                source: r'elements_images/Tm.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Yb ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredfive'
            Image:
                source: r'elements_images/Yb.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Lu ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredsix'
            Image:
                source: r'elements_images/Lu.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Label:
            text: "189"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            text: "190"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            text: "191"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            text: '[color=000000]     [size=12]series[/size]\\n[size=38][b]*Ac[/color][/size][/b]'
            markup:True
            background_normal: ''
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: .01568627,.2666666666,.7647,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            ############ Ac ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_ninetytwo'
            Image:
                source: r'elements_images/Ac.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Th ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredseven'
            Image:
                source: r'elements_images/Th.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Pa ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredeight'
            Image:
                source: r'elements_images/Pa.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ U ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundrednine'
            Image:
                source: r'elements_images/U.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Np ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredten'
            Image:
                source: r'elements_images/Np.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Pu ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredeleven'
            Image:
                source: r'elements_images/Pu.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Am ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredtwelve'
            Image:
                source: r'elements_images/Am.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Cm ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredthirteen'
            Image:
                source: r'elements_images/Cm.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Bk ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredfourteen'
            Image:
                source: r'elements_images/Bk.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Cf ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredfifteen'
            Image:
                source: r'elements_images/Cf.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Es ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredsixteen'
            Image:
                source: r'elements_images/Es.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Fm ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredseventeen'
            Image:
                source: r'elements_images/Fm.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Md ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredeighteen'
            Image:
                source: r'elements_images/Md.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ No ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundrednineteen'
            Image:
                source: r'elements_images/No.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            ############ Lr ###################
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_hundredtwenty'
            Image:
                source: r'elements_images/Lr.png'
                size_hint: .1,.1
                y: self.parent.y
                x: self.parent.x
                allow_stretch: True
                keep_ratio: False
        Button:
            text: "208"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            text: "209"
            markup:True
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    size: self.size
                    pos: self.pos
    Spinner:
        id: my_spinner
        size_hint: None, None
        size: 120, 44
        pos_hint: {'center': (.84, .86)}
        text: 'Home'
        values: "Standard State","Oxidation","Electronegativity"
        on_text:
            if my_spinner.text == "Standard State":root.manager.current = 'std_state'
            elif my_spinner.text == "Oxidation":root.manager.current = 'oxidation'
            elif my_spinner.text == "Electronegativity":root.manager.current = 'electro'
<ScreenThree>:
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'bottom'
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .20,.35
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/hydrogen-2.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/hydrogen_orbital.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'top'
        Image:
            source: r'text_files/hydrogen_d.png'
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFour>:
	on_enter:
		screenfour_video.state= 'play'
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'center'
        Video:
            id: screenfour_video
            source: r'Video/Helium.mp4'
            allow_stretch: 'True'
            allow_fullscreen:'True'
            # keep_ratio: 'False'
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'top'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.ids.screenfour_video.state = 'stop'
                root.manager.current = 'screen_two'
<ScreenFive>:
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/Lithium.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.2
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/Lithium_orbital.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'top'
        Image:
            source: r'text_files/lithium_d.png'
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSix>:
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/beryllium.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            # source: r'Media Files/hydrogen_orbital.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'top'
        Image:
            source: r'text_files/Beryllium_d.png'
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeven>:
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'bottom'
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/Boron.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/boron_orbital.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'top'
        Image:
            source: r'text_files/Boron_d.png'
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEight>:
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'bottom'
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            # source: r'Media Files/Carbon.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/carbon_orbital.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'top'
        Image:
            source: r'text_files/hydrogen_d.png'
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Nitrogen"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Oxygen"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEleven>:
	on_enter:
		screeneleven_video.state= 'play'
    AnchorLayout:
        anchor_x : 'center'
        anchor_y : 'center'
        Video:
            id: screeneleven_video
            source: r'Video/Fluorine.mp4'
            allow_stretch: 'True'
            allow_fullscreen:'True'
            keep_ratio: 'False'
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'top'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.ids.screeneleven_video.state = 'stop'
                root.manager.current = 'screen_two'
    # FloatLayout:
    #     Label:
    #         size_hint: .2,.1
    #         text: "Fluorine"
    #         pos_hint:{"center_x":0.5,"center_y":0.5}
    #     Button:
    #         size_hint: .1,.05
    #         size: 15,5
    #         text: "Back"
    #         pos_hint:{"left":1,"bottom":0}
    #         on_press:
    #             root.manager.transition.direction = 'left'
    #             root.manager.transition.duration = 0
    #             root.manager.current = 'screen_two'
<ScreenTwelve>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Neon"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Sodium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourteen>:
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/mAGNESIUM2.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFifteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Aluminium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Silicon"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventeen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Phosphorous"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEighteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Sulphur"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNineteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Chlorine"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwenty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Argon"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentyone>:
    AnchorLayout:
        anchor_x : 'right'
        anchor_y : 'top'
        # orientation: "vertical"
        Image:
            id: gif
            canvas:
                Color:
                    rgba: 0, 0, 0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: .15,.3
            allow_stretch: True
            keep_ratio: False
            source: r'Media Files/Potassium_orbitsl.gif'
            anim_delay: 0.10
            anim_loop: 100
    AnchorLayout:
        anchor_x : 'left'
        anchor_y : 'bottom'
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Calcium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Scandium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Titanium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Vanadium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Chromium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Manganese"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Iron"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenTwentynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Cobalt"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Nickel"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Copper"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Zinc"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Gallium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Germanium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Arsenic"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Selenium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Bromine"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Krypton"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenThirtynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Rubidium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Strontium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Yttrium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Zirconium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Niobium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Molybdenum"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Technetium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Ruthenium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Rhodium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Palladium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFourtynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Silver"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFifty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Cadmium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Indium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Tin"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Antimony"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Tellurium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Iodine"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Xenon"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Cesium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Barium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenFiftynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Hafnium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Tantalum"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Tungsten"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Rhenium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Osmium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Iridium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Platinum"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Gold"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Mercury"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Thalium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSixtynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Lead"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventy>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Bismuth"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Polonium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Astatine"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Radon"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Francium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Radium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Rutherfordium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Dubnium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Seaborgium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenSeventynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Bohrium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEighty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Hassium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Meitnerium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Darmstadium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Roentgenium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Copernicium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Nihonium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Flerovium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Moscovium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Livermorium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenEightynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Tennessine"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinety>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Oganesson"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetyone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Lanthanum"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetytwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Actinium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetythree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Cerium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetyfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Praseodymium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetyfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Neodymium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetysix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Promethium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetyseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Samarium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetyeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Europium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenNinetynine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Gadolinium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundred>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Terbium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredone>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Dysprosium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredtwo>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Holmium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredthree>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Erbium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredfour>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Thulium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredfive>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Ytterbium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredsix>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Lutetium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredseven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Thorium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredeight>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Protactinium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundrednine>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Uranium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredten>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Neptunium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredeleven>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Plutonium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredtwelve>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Americium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredthirteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Curium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredfourteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Berkelium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredfifteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Californium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredsixteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Einstenium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredseventeen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Fermium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredeighteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Mendelevium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundrednineteen>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Nobelium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
<ScreenHundredtwenty>:
    FloatLayout:
        Label:
            size_hint: .2,.1
            text: "Lawrencium"
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Button:
            size_hint: .1,.05
            size: 15,5
            text: "Back"
            pos_hint:{"left":1,"bottom":0}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0
                root.manager.current = 'screen_two'
""")


# Create a class for all screens in which you can include
# helpful methods specific to that screen





class ScreenOne(Screen):
    pass

class IntroScreen(Screen):
    pass


class Electro(Screen):
    pass


class Oxidation(Screen):
    pass


class StdState(Screen):
    pass

class ScreenTwo(Screen):
    # def val1(self):
    #     self.ScreenFour.ids.testid.state = 'Play'
    #     self.screen_manager.current = 'ScreenTwo'

    # def __init__(self, **kw):
    #     super().__init__(**kw)
    #     self.sound = SoundLoader.load('audio/lithium_raw.wav')
    #
    # def music(self):
    #     if self.sound:
    #         self.sound.play()
    pass


class ScreenThree(Screen):
    pass


class ScreenFour(Screen):
    # def stop(self):
    #     self.screen_four.testid.state = 'stop'
    #     self.screen_four.screen_manager.current = 'Screen_Two'
    pass


class ScreenFive(Screen):
    pass


# def __init__(self, **kw):
#     super().__init__(**kw)
#     self.sound = SoundLoader.load('audio/lithium_raw.wav')
#
# def stop_music(self):
#     self.sound.stop()


class ScreenSix(Screen):
    pass


class ScreenSeven(Screen):
    pass


class ScreenEight(Screen):
    pass


class ScreenNine(Screen):
    pass


class ScreenTen(Screen):
    pass


class ScreenEleven(Screen):
    pass


class ScreenTwelve(Screen):
    pass


class ScreenThirteen(Screen):
    pass


class ScreenFourteen(Screen):
    pass


class ScreenFifteen(Screen):
    pass


class ScreenSixteen(Screen):
    pass


class ScreenSeventeen(Screen):
    pass


class ScreenEighteen(Screen):
    pass


class ScreenNineteen(Screen):
    pass


class ScreenTwenty(Screen):
    pass


class ScreenTwentyone(Screen):
    pass


class ScreenTwentytwo(Screen):
    pass


class ScreenTwentythree(Screen):
    pass


class ScreenTwentyfour(Screen):
    pass


class ScreenTwentyfive(Screen):
    pass


class ScreenTwentysix(Screen):
    pass


class ScreenTwentyseven(Screen):
    pass


class ScreenTwentyeight(Screen):
    pass


class ScreenTwentynine(Screen):
    pass


class ScreenThirty(Screen):
    pass


class ScreenThirtyone(Screen):
    pass


class ScreenThirtytwo(Screen):
    pass


class ScreenThirtythree(Screen):
    pass


class ScreenThirtyfour(Screen):
    pass


class ScreenThirtyfive(Screen):
    pass


class ScreenThirtysix(Screen):
    pass


class ScreenThirtyseven(Screen):
    pass


class ScreenThirtyeight(Screen):
    pass


class ScreenThirtynine(Screen):
    pass


class ScreenFourty(Screen):
    pass


class ScreenFourtyone(Screen):
    pass


class ScreenFourtytwo(Screen):
    pass


class ScreenFourtythree(Screen):
    pass


class ScreenFourtyfour(Screen):
    pass


class ScreenFourtyfive(Screen):
    pass


class ScreenFourtysix(Screen):
    pass


class ScreenFourtyseven(Screen):
    pass


class ScreenFourtyeight(Screen):
    pass


class ScreenFourtynine(Screen):
    pass


class ScreenFifty(Screen):
    pass


class ScreenFiftyone(Screen):
    pass


class ScreenFiftytwo(Screen):
    pass


class ScreenFiftythree(Screen):
    pass


class ScreenFiftyfour(Screen):
    pass


class ScreenFiftyfive(Screen):
    pass


class ScreenFiftysix(Screen):
    pass


class ScreenFiftyseven(Screen):
    pass


class ScreenFiftyeight(Screen):
    pass


class ScreenFiftynine(Screen):
    pass


class ScreenSixty(Screen):
    pass


class ScreenSixtyone(Screen):
    pass


class ScreenSixtytwo(Screen):
    pass


class ScreenSixtythree(Screen):
    pass


class ScreenSixtyfour(Screen):
    pass


class ScreenSixtyfive(Screen):
    pass


class ScreenSixtysix(Screen):
    pass


class ScreenSixtyseven(Screen):
    pass


class ScreenSixtyeight(Screen):
    pass


class ScreenSixtynine(Screen):
    pass


class ScreenSeventy(Screen):
    pass


class ScreenSeventyone(Screen):
    pass


class ScreenSeventytwo(Screen):
    pass


class ScreenSeventythree(Screen):
    pass


class ScreenSeventyfour(Screen):
    pass


class ScreenSeventyfive(Screen):
    pass


class ScreenSeventysix(Screen):
    pass


class ScreenSeventyseven(Screen):
    pass


class ScreenSeventyeight(Screen):
    pass


class ScreenSeventynine(Screen):
    pass


class ScreenEighty(Screen):
    pass


class ScreenEightyone(Screen):
    pass


class ScreenEightytwo(Screen):
    pass


class ScreenEightythree(Screen):
    pass


class ScreenEightyfour(Screen):
    pass


class ScreenEightyfive(Screen):
    pass


class ScreenEightysix(Screen):
    pass


class ScreenEightyseven(Screen):
    pass


class ScreenEightyeight(Screen):
    pass


class ScreenEightynine(Screen):
    pass


class ScreenNinety(Screen):
    pass


class ScreenNinetyone(Screen):
    pass


class ScreenNinetytwo(Screen):
    pass


class ScreenNinetythree(Screen):
    pass


class ScreenNinetyfour(Screen):
    pass


class ScreenNinetyfive(Screen):
    pass


class ScreenNinetysix(Screen):
    pass


class ScreenNinetyseven(Screen):
    pass


class ScreenNinetyeight(Screen):
    pass


class ScreenNinetynine(Screen):
    pass


class ScreenHundred(Screen):
    pass


class ScreenHundredone(Screen):
    pass


class ScreenHundredtwo(Screen):
    pass


class ScreenHundredthree(Screen):
    pass


class ScreenHundredfour(Screen):
    pass


class ScreenHundredfive(Screen):
    pass


class ScreenHundredsix(Screen):
    pass


class ScreenHundredseven(Screen):
    pass


class ScreenHundredeight(Screen):
    pass


class ScreenHundrednine(Screen):
    pass


class ScreenHundredten(Screen):
    pass


class ScreenHundredeleven(Screen):
    pass


class ScreenHundredtwelve(Screen):
    pass


class ScreenHundredthirteen(Screen):
    pass


class ScreenHundredfourteen(Screen):
    pass


class ScreenHundredfifteen(Screen):
    pass


class ScreenHundredsixteen(Screen):
    pass


class ScreenHundredseventeen(Screen):
    pass


class ScreenHundredeighteen(Screen):
    pass


class ScreenHundrednineteen(Screen):
    pass


class ScreenHundredtwenty(Screen):
    pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(IntroScreen(name="intro_screen"))
screen_manager.add_widget(Electro(name="electro"))
screen_manager.add_widget(Oxidation(name="oxidation"))
screen_manager.add_widget(StdState(name="std_state"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))
screen_manager.add_widget(ScreenFive(name="screen_five"))
screen_manager.add_widget(ScreenSix(name="screen_six"))
screen_manager.add_widget(ScreenSeven(name="screen_seven"))
screen_manager.add_widget(ScreenEight(name="screen_eight"))
screen_manager.add_widget(ScreenNine(name="screen_nine"))
screen_manager.add_widget(ScreenTen(name="screen_ten"))
screen_manager.add_widget(ScreenEleven(name="screen_eleven"))
screen_manager.add_widget(ScreenTwelve(name="screen_twelve"))
screen_manager.add_widget(ScreenThirteen(name="screen_thirteen"))
screen_manager.add_widget(ScreenFourteen(name="screen_fourteen"))
screen_manager.add_widget(ScreenFifteen(name="screen_fifteen"))
screen_manager.add_widget(ScreenSixteen(name="screen_sixteen"))
screen_manager.add_widget(ScreenSeventeen(name="screen_seventeen"))
screen_manager.add_widget(ScreenEighteen(name="screen_eighteen"))
screen_manager.add_widget(ScreenNineteen(name="screen_nineteen"))
screen_manager.add_widget(ScreenTwenty(name="screen_twenty"))
screen_manager.add_widget(ScreenTwentyone(name="screen_twentyone"))
screen_manager.add_widget(ScreenTwentytwo(name="screen_twentytwo"))
screen_manager.add_widget(ScreenTwentythree(name="screen_twentythree"))
screen_manager.add_widget(ScreenTwentyfour(name="screen_twentyfour"))
screen_manager.add_widget(ScreenTwentyfive(name="screen_twentyfive"))
screen_manager.add_widget(ScreenTwentysix(name="screen_twentysix"))
screen_manager.add_widget(ScreenTwentyseven(name="screen_twentyseven"))
screen_manager.add_widget(ScreenTwentyeight(name="screen_twentyeight"))
screen_manager.add_widget(ScreenTwentynine(name="screen_twentynine"))
screen_manager.add_widget(ScreenThirty(name="screen_thirty"))
screen_manager.add_widget(ScreenThirtyone(name="screen_thirtyone"))
screen_manager.add_widget(ScreenThirtytwo(name="screen_thirtytwo"))
screen_manager.add_widget(ScreenThirtythree(name="screen_thirtythree"))
screen_manager.add_widget(ScreenThirtyfour(name="screen_thirtyfour"))
screen_manager.add_widget(ScreenThirtyfive(name="screen_thirtyfive"))
screen_manager.add_widget(ScreenThirtysix(name="screen_thirtysix"))
screen_manager.add_widget(ScreenThirtyseven(name="screen_thirtyseven"))
screen_manager.add_widget(ScreenThirtyeight(name="screen_thirtyeight"))
screen_manager.add_widget(ScreenThirtynine(name="screen_thirtynine"))
screen_manager.add_widget(ScreenFourty(name="screen_fourty"))
screen_manager.add_widget(ScreenFourtyone(name="screen_fourtyone"))
screen_manager.add_widget(ScreenFourtytwo(name="screen_fourtytwo"))
screen_manager.add_widget(ScreenFourtythree(name="screen_fourtythree"))
screen_manager.add_widget(ScreenFourtyfour(name="screen_fourtyfour"))
screen_manager.add_widget(ScreenFourtyfive(name="screen_fourtyfive"))
screen_manager.add_widget(ScreenFourtysix(name="screen_fourtysix"))
screen_manager.add_widget(ScreenFourtyseven(name="screen_fourtyseven"))
screen_manager.add_widget(ScreenFourtyeight(name="screen_fourtyeight"))
screen_manager.add_widget(ScreenFourtynine(name="screen_fourtynine"))
screen_manager.add_widget(ScreenFifty(name="screen_fifty"))
screen_manager.add_widget(ScreenFiftyone(name="screen_fiftyone"))
screen_manager.add_widget(ScreenFiftytwo(name="screen_fiftytwo"))
screen_manager.add_widget(ScreenFiftythree(name="screen_fiftythree"))
screen_manager.add_widget(ScreenFiftyfour(name="screen_fiftyfour"))
screen_manager.add_widget(ScreenFiftyfive(name="screen_fiftyfive"))
screen_manager.add_widget(ScreenFiftysix(name="screen_fiftysix"))
screen_manager.add_widget(ScreenFiftyseven(name="screen_fiftyseven"))
screen_manager.add_widget(ScreenFiftyeight(name="screen_fiftyeight"))
screen_manager.add_widget(ScreenFiftynine(name="screen_fiftynine"))
screen_manager.add_widget(ScreenSixty(name="screen_sixty"))
screen_manager.add_widget(ScreenSixtyone(name="screen_sixtyone"))
screen_manager.add_widget(ScreenSixtytwo(name="screen_sixtytwo"))
screen_manager.add_widget(ScreenSixtythree(name="screen_sixtythree"))
screen_manager.add_widget(ScreenSixtyfour(name="screen_sixtyfour"))
screen_manager.add_widget(ScreenSixtyfive(name="screen_sixtyfive"))
screen_manager.add_widget(ScreenSixtysix(name="screen_sixtysix"))
screen_manager.add_widget(ScreenSixtyseven(name="screen_sixtyseven"))
screen_manager.add_widget(ScreenSixtyeight(name="screen_sixtyeight"))
screen_manager.add_widget(ScreenSixtynine(name="screen_sixtynine"))
screen_manager.add_widget(ScreenSeventy(name="screen_seventy"))
screen_manager.add_widget(ScreenSeventyone(name="screen_seventyone"))
screen_manager.add_widget(ScreenSeventytwo(name="screen_seventytwo"))
screen_manager.add_widget(ScreenSeventythree(name="screen_seventythree"))
screen_manager.add_widget(ScreenSeventyfour(name="screen_seventyfour"))
screen_manager.add_widget(ScreenSeventyfive(name="screen_seventyfive"))
screen_manager.add_widget(ScreenSeventysix(name="screen_seventysix"))
screen_manager.add_widget(ScreenSeventyseven(name="screen_seventyseven"))
screen_manager.add_widget(ScreenSeventyeight(name="screen_seventyeight"))
screen_manager.add_widget(ScreenSeventynine(name="screen_seventynine"))
screen_manager.add_widget(ScreenEighty(name="screen_eighty"))
screen_manager.add_widget(ScreenEightyone(name="screen_eightyone"))
screen_manager.add_widget(ScreenEightytwo(name="screen_eightytwo"))
screen_manager.add_widget(ScreenEightythree(name="screen_eightythree"))
screen_manager.add_widget(ScreenEightyfour(name="screen_eightyfour"))
screen_manager.add_widget(ScreenEightyfive(name="screen_eightyfive"))
screen_manager.add_widget(ScreenEightysix(name="screen_eightysix"))
screen_manager.add_widget(ScreenEightyseven(name="screen_eightyseven"))
screen_manager.add_widget(ScreenEightyeight(name="screen_eightyeight"))
screen_manager.add_widget(ScreenEightynine(name="screen_eightynine"))
screen_manager.add_widget(ScreenNinety(name="screen_ninety"))
screen_manager.add_widget(ScreenNinetyone(name="screen_ninetyone"))
screen_manager.add_widget(ScreenNinetytwo(name="screen_ninetytwo"))
screen_manager.add_widget(ScreenNinetythree(name="screen_ninetythree"))
screen_manager.add_widget(ScreenNinetyfour(name="screen_ninetyfour"))
screen_manager.add_widget(ScreenNinetyfive(name="screen_ninetyfive"))
screen_manager.add_widget(ScreenNinetysix(name="screen_ninetysix"))
screen_manager.add_widget(ScreenNinetyseven(name="screen_ninetyseven"))
screen_manager.add_widget(ScreenNinetyeight(name="screen_ninetyeight"))
screen_manager.add_widget(ScreenNinetynine(name="screen_ninetynine"))
screen_manager.add_widget(ScreenHundred(name="screen_hundred"))
screen_manager.add_widget(ScreenHundredone(name="screen_hundredone"))
screen_manager.add_widget(ScreenHundredtwo(name="screen_hundredtwo"))
screen_manager.add_widget(ScreenHundredthree(name="screen_hundredthree"))
screen_manager.add_widget(ScreenHundredfour(name="screen_hundredfour"))
screen_manager.add_widget(ScreenHundredfive(name="screen_hundredfive"))
screen_manager.add_widget(ScreenHundredsix(name="screen_hundredsix"))
screen_manager.add_widget(ScreenHundredseven(name="screen_hundredseven"))
screen_manager.add_widget(ScreenHundredeight(name="screen_hundredeight"))
screen_manager.add_widget(ScreenHundrednine(name="screen_hundrednine"))
screen_manager.add_widget(ScreenHundredten(name="screen_hundredten"))
screen_manager.add_widget(ScreenHundredeleven(name="screen_hundredeleven"))
screen_manager.add_widget(ScreenHundredtwelve(name="screen_hundredtwelve"))
screen_manager.add_widget(ScreenHundredthirteen(name="screen_hundredthirteen"))
screen_manager.add_widget(ScreenHundredfourteen(name="screen_hundredfourteen"))
screen_manager.add_widget(ScreenHundredfifteen(name="screen_hundredfifteen"))
screen_manager.add_widget(ScreenHundredsixteen(name="screen_hundredsixteen"))
screen_manager.add_widget(ScreenHundredseventeen(name="screen_hundredseventeen"))
screen_manager.add_widget(ScreenHundredeighteen(name="screen_hundredeighteen"))
screen_manager.add_widget(ScreenHundrednineteen(name="screen_hundrednineteen"))
screen_manager.add_widget(ScreenHundredtwenty(name="screen_hundredtwenty"))


class Pt_mod_App(App):

    def build(self):
        return screen_manager


pro_app = Pt_mod_App()
pro_app.run()