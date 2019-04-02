import kivy
kivy.require('1.10.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.slider import Slider


class Controller(FloatLayout):
    """
    Base class for sliders
    """


class ControllerApp(App):

    def build(self):
        return Controller()


if __name__ == '__main__':
    ControllerApp().run()