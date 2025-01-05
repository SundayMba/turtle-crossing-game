from turtle import Turtle

STARTING_POSITION = (0, -310)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, player, play_music):
        super().__init__()
        self.shape(player)
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.play_music = play_music

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        self.play_music()

    def go_down(self):
        self.backward(MOVE_DISTANCE)
        self.play_music()
     
    def go_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
        self.play_music()

    def go_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
        self.play_music()
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
