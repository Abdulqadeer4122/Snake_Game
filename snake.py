import turtle as t
SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20


class Snake:
    def __init__(self):
        self.body_segments=[]
        self.creat_snake()
        self.head = self.body_segments[0]

    def creat_snake(self):
        for position in SNAKE_POSITION:
            self.create_segment(position)

    def create_segment(self,position):
        snake = t.Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.body_segments.append(snake)


    def extend_snake(self):
        self.create_segment(self.body_segments[-1].position())

    def snake_reset(self):
        for seg in self.body_segments:
            seg.goto(1000, 1000)
        self.body_segments.clear()
        self.creat_snake()
        self.head = self.body_segments[0]

    def move(self):
        for segment in range(len(self.body_segments) - 1, 0, -1):
            # this line get the x coordinate value of the second last element in first iteration
            x_new = self.body_segments[segment - 1].xcor()
            # this line get the y coordinate value of the second last element in first iteration
            y_new = self.body_segments[segment - 1].ycor()
            # this line update the value of coordinate of last snake segment with the second last element and then so on
            self.body_segments[segment].goto(x_new, y_new)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)





