import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class myCallback(Widget):

    def my_callBack(self, *args):
        msg = "I have been bound to an event, and now I have been called!"
        self.label = Label(text=msg)
        self.label.center_x = 400
        self.label.center_y = 400
        self.add_widget(self.label)

class MyEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def do_something(self, value):
        # when do_something is called, the 'on_test' event will be
        # dispatched with the value
        self.dispatch('on_test', value)

    def on_test(self, *args):
        for arg in args:
            print("I am dispatched: {}".format(arg))

class MyApp(App):

    def build(self):
        call = myCallback()
        # create event dispatcher
        event = MyEventDispatcher()
        # bind an event to the event dispatcher method
        event.bind(on_test=call.my_callBack)
        # Call event, which calls method with bound event
        event.do_something('test')
        # return class showing the result of the bound event
        return call


if __name__ == '__main__':
    MyApp().run()

