import time
from turtle import Screen
from kamlumbaga import Kamlumbaga
from cars import Car
from game import Game
import random


def main():
    """Starts the game."""

    # Create a screen and set its properties
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('gray')
    screen.tracer(0)

    # Create a Kamlumbaga and a list of cars
    kaplumba = Kamlumbaga()
    game = Game()
    cars = Car.create_random_cars(10)
    game.level()

    def restart_game():
        """Restart the game when 'r' key is pressed."""
        if game.game_over:
            game.clear()
            game.sayac = 0
            game.game_over = False
            game.level()
            kaplumba.start()

    # Listen for keyboard events
    screen.listen()
    screen.onkeypress(kaplumba.go_forward, 'Up')
    screen.onkeypress(kaplumba.go_backward, 'Down')
    screen.onkeypress(kaplumba.go_forward, 'w')
    screen.onkeypress(kaplumba.go_backward, 's')
    screen.onkeypress(restart_game, 'r')

    game_on = True
    # Start the game loop
    while game_on:
        time.sleep(0.05)
        screen.update()

        if kaplumba.ycor() > 280:
            game.sayac += 1
            kaplumba.start()
            game.level()
            screen.update()

        for car in cars:
            car.move()
            if car.distance(kaplumba) < 20:
                game.game_over()
                game.sayac = 0
                screen.exitonclick()

        for car in cars:
            if car.xcor() < -300:
                car.goto(x=random.randint(250, 290), y=random.randint(-250, 265))


if __name__ == '__main__':
    main()
