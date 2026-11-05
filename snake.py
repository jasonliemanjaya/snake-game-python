from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self, x=0, y=0):
        for _ in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x, y)
            x -= 20
            self.add_segment(snake)

    def add_segment(self, snake):
        self.segments.append(snake)

    def extend(self):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(self.segments[-1].position())
        self.add_segment(snake)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_numm in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_numm - 1].xcor()
            new_y = self.segments[seg_numm - 1].ycor()
            self.segments[seg_numm].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)