from turtle import Turtle

# CONSTANTS
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # creates the initial body of a snake
    def create_snake(self):
        for position in START_POSITION:
            self.new_body(position)

    def new_body(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Extends the body of the snake after getting its food
    def extend(self):
        x_pos = self.segments[-1].xcor()
        y_pos = self.segments[-1].ycor()
        self.new_body((x_pos, y_pos))

    # makes the snake to move with all its segments continuously
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # event listener func 'keyup'
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    # event listener func 'keydown'
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    # event listener func 'key_right'
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    # event listener func 'key_left'
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
