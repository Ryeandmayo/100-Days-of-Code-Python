from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_up():
    tim.seth(90)
    tim.forward(10)
def move_left():
    tim.seth(180)
    tim.forward(10)
def move_down():
    tim.seth(270)
    tim.forward(10)
def move_right():
    tim.seth(0)
    tim.forward(10)
screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()