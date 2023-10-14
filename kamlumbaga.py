from turtle import Turtle

class Kamlumbaga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.start()

    def start(self):
        """Move the Kamlumbaga to the starting position."""
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        """Move the Kamlumbaga forward."""
        self.forward(10)

    def go_forward(self):
        """Move the Kamlumbaga forward when a key is pressed."""
        self.forward(10)

    def go_backward(self):
        """Move the Kamlumbaga backward when a key is pressed."""
        self.backward(10)
