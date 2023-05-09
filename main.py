import time
from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
from boundary import Boundary

# sets the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create boundary using boundary class
boundary = Boundary()

snake = Snake()
food = Food()
score = ScoreBoard()

# screen event listeners
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

# loop that runs the game
movement = True
while movement:
    screen.update()
    time.sleep(0.14)
    snake.move()

    # catch the food and  grow big
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_board()
        screen.update()
        snake.extend()

    # game over on hitting the boundary
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        movement = False
        score.game_over()

    # game over on hitting its body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            movement = False
            score.game_over()

screen.exitonclick()
