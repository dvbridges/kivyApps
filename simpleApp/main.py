import kivy
kivy.require('1.10.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class nestedLayout(GridLayout):
    def __init__(self, **kwargs):
        super(nestedLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(LoginScreen())
        self.add_widget(LoginScreen())

class MyApp(App):

    def build(self):
        return nestedLayout()


if __name__ == '__main__':
    MyApp().run()
