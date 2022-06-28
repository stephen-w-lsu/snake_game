from turtle import Turtle

STARTING_SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.seg_list = []
        self.create_snake()
        self.head = self.seg_list[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(STARTING_SEGMENTS):
            self.add_segment(x, y)
            x -= 20

    def add_segment(self, x_cor, y_cor):
        self.seg = Turtle("square")
        self.seg.color("white")
        self.seg.penup()
        self.seg.setposition(x_cor, y_cor)
        self.seg_list.append(self.seg)

    def extend(self):
        self.add_segment(self.seg_list[-1].xcor(), self.seg_list[-1].ycor())

    def move(self):
        for seg_num in range(len(self.seg_list)-1, 0, -1):
            self.seg_list[seg_num].goto(self.seg_list[seg_num-1].xcor(), self.seg_list[seg_num-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

