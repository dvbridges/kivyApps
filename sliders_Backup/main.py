import kivy
kivy.require('1.10.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock

class Level(Slider):
    """
    A Level class for controlling sound levels
    """

    def __init__(self, **kwargs):
        super(Level, self).__init__(**kwargs)
        Slider(min=0, max=100, value=0, orientation='vertical')
        

class LevelText(Label):
    """
    A class for displaying sound levels as strings
    """

    textCtrl = StringProperty("0")

    def __init__(self, **kwargs):
        super(LevelText, self).__init__(**kwargs)
        Label(text="0")
        self.font_size = 50

    def updateText(self, text):
        self.text = str(int(text))


class Equalizer(BoxLayout):
    """
    Class for laying out EQ sliders
    """
    def __init__(self, **kwargs):
        super(Equalizer, self).__init__(**kwargs)

        self.bass = Level(orientation='vertical', cursor_image="bass.png")
        self.mid = Level(orientation='vertical', cursor_image="mid.jpeg")
        self.treble = Level(orientation='vertical', cursor_image="treble.png")
        self.add_widget(self.bass)
        self.add_widget(self.mid)
        self.add_widget(self.treble)


class EQValues(BoxLayout):
    """
    Class for laying out EQ values
    """
    def __init__(self, **kwargs):
        super(EQValues, self).__init__(**kwargs)
  
        self.bass = LevelText()
        self.mid = LevelText()
        self.treble = LevelText()

        self.add_widget(self.bass)
        self.add_widget(self.mid)
        self.add_widget(self.treble)
        self.size_hint = (1, .25)

class EQLabels(BoxLayout):
    """
    Class for laying out EQ Labels
    """
    def __init__(self, **kwargs):
        super(EQLabels, self).__init__(**kwargs)
  
        self.bass = LevelText()
        self.mid = LevelText()
        self.treble = LevelText()

        self.bass.text = "Bass"
        self.mid.text = "Mid"
        self.treble.text = "Treble"

        self.add_widget(self.bass)
        self.add_widget(self.mid)
        self.add_widget(self.treble)
        self.size_hint = (1, .25)

class MasterEqualizer(BoxLayout):
    """
    MAster sizer for laying out EQ sliders, values and labels
    """
    def __init__(self, **kwargs):
        super(MasterEqualizer, self).__init__(**kwargs)
        self.values = EQValues(orientation='horizontal')
        self.sliders = Equalizer(orientation='horizontal')
        self.labels = EQLabels(orientation='horizontal')

        self.add_widget(self.values)
        self.add_widget(self.sliders)      
        self.add_widget(self.labels)

    def update(self, instance):
        self.values.bass.updateText(self.sliders.bass.value)
        self.values.mid.updateText(self.sliders.mid.value)
        self.values.treble.updateText(self.sliders.treble.value)

# The app class
class SliderExample(App):
    def build(self):
        equalizer = MasterEqualizer(orientation='vertical')
        Clock.schedule_interval(equalizer.update, 1/60)  # call every second
        return equalizer
 

# Run the app       
if __name__ == '__main__':
    SliderExample().run()