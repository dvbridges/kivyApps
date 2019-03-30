
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint, random
from kivy.uix.label import Label


class PongBall(Widget):
    
    # velocity of the ball on the x,y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongBat(Widget):
    
    score = NumericProperty(0)
    
    def setColor(self, color):
        self.color = color

    def bounce_ball(self, ball):
        if self.collide_widget(ball):           
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            if ball.center_y > self.top or ball.center_y < self.y:
                bounced = Vector(vx, vy)
            else:
                bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            # randomize ball color
            ball.color = self.randomize_ball_color()
    
    def randomize_ball_color(self):
        return (random(), random(), random(), 1)


class PongGame(Widget):
    
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def set_bat_color(self):
        self.player1.setColor((249/255.0, 41/255.0, 180/255.0, 255/255.0))
        self.player2.setColor((41/255.0, 249/255.0, 69/255.0, 255/255.0))
    
    def set_text_color(self):
        self.score1.color = (249/255.0, 41/255.0, 180/255.0, 255/255.0)
        self.score2.color = (41/255.0, 249/255.0, 69/255.0, 255/255.0)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def serve_bats(self):
        self.player1.center = (25, 0)
        self.player2.center = (self.width, 0)

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

    def update(self, dt):
        # call ball.move
        self.ball.move()
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
            self.score2.text = str(self.player2.score)
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
            self.score1.text = str(self.player1.score)
        if self.player1.score > 1 or self.player2.score > 10:
            loser = "Player 1"
            if self.player1.score > self.player2.score:
                loser = "Player 2"
            self.label = Label(text="You LOSE\n{}".format(loser))
            self.label.set_center_x(self.center_x)
            self.label.set_center_y(self.center_y+20)
            self.label.color = (1,0,0,1)
            self.label.font_size = 75
            self.label.halign = 'center'
            self.add_widget(self.label)
            return False


class PongApp(App):

    def build(self):
        game = PongGame()
        game.set_bat_color()
        game.set_text_color()
        game.serve_ball()
        game.serve_bats()
        event = Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    PongApp().run()

