from turtle import Turtle, Screen

class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sayac = 0

    def game_over(self):
        """Display a 'Game Over' message on the screen."""
        self.color("red")
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Courier', 24, 'bold'))

    def level(self):
        """Display the current level on the screen."""
        self.clear()
        self.color("black")
        self.goto(-280, 280)
        self.write(f'Level: {self.sayac}', align='left', font=('Courier', 12, 'bold'))


