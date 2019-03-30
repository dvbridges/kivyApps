import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget


class myCallback(Widget):

    def my_callBack(self, dt):
        print("My callback is called every second! {}".format(dt))


class MyApp(App):

    def build(self):
        call = myCallback()
        # Clock.schedule_interval(call.my_callBack, 1)  # call every second
        # Clock.schedule_once(call.my_callBack, 1)  # or call once
        
        # or create a trigger to call your event
        trigger = Clock.create_trigger(call.my_callBack)
        trigger()
        return


if __name__ == '__main__':
    MyApp().run()

