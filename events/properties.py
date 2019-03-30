import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget, StringProperty
from kivy.uix.label import Label
import random 


class MyWidget(Widget):
    text = StringProperty('MyText')
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
    
    def my_callback(self, evt):
        self.text = "Changing properties triggers events: {}".format(random.random())

    def on_text(self, *args):
        """The on_<property_Event> is triggered when property changes"""
        print(self.text)

class MyApp(App):

    def build(self):
        wijj = MyWidget()
        Clock.schedule_interval(wijj.my_callback, 1)
        return wijj


if __name__ == '__main__':
    MyApp().run()

