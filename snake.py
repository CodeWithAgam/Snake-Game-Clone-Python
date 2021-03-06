from turtle import Turtle


START_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake: 
    def __init__(self):
        """Function to initialize the Snake"""
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]
        self.distance = 20

    def create_snake(self):
        """Function to create the snake"""
        for pos in START_POSITIONS:
            self.add_box(pos)
    
    def add_box(self, pos):
        """Function to add a box to the snake"""
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.boxes.append(t)

    def extend(self):
        """Function to extend the snake"""
        self.add_box(self.boxes[-1].position())

    def reset(self):
        """Function to reset the snake"""
        for box in self.boxes:
            box.goto(1000, 1000)
        self.boxes.clear()
        self.create_snake()
        self.head = self.boxes[0]

    def move(self):
        """Function to move the snake"""
        for box in range((len(self.boxes) - 1), 0, -1):
            x, y = self.boxes[box - 1].pos()
            self.boxes[box].goto(x, y)
        self.head.forward(self.distance)
    
    def forward(self):
        """Function to move the snake forward"""
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def backward(self):
        """Function to move the snake backward"""
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self):
        """Function to move the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Function to move the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
