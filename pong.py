from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Pong(Widget):
    def __init__(self, **kwargs):
        super(Pong, self).__init__(**kwargs)

"""class Ball(Widget):
    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)
        velocity_x = NumericProperty(0)
        velocity_Y = NumericProperty(0)
        velocity = ReferenceListProperty(velocity_x, velocity_Y)

        def move(self):
            self.pos = Vector(*self.velocity) + self.pos"""



class Ping(App):
    def build(self):
        window = Pong()
        return window
        ball = Ball()
        
if __name__ == "__main__":
    Ping().run()