import random
from turtle import Turtle

COLORS = ["red", "green", "blue", "yellow", "orange", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.speed(0.1)
        x, y, z = self.random_position()
        self.goto(x, y)
        self.speed(z)

    def move(self):
        """Moves the car forward with its specified speed."""
        self.forward(10)

    @classmethod
    def create_random_cars(cls, num_cars):
        """Creates a list of random cars."""
        cars = [cls() for _ in range(num_cars)]
        return cars

    def random_position(self):
        """Generates a random position and speed for a car."""
        x = random.randint(-200, 290)
        y = random.randint(-250, 270)
        z = random.uniform(0.1, 0.5)
        return x, y, z
