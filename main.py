from turtle import Turtle, Screen
import random


def set_up():
    default_x = -150
    for x in range(7):
        turtle = Turtle(shape="turtle")
        turtle_list.append(turtle)
        turtle.penup()
        turtle.color(color_list[x])
        turtle.goto(-200, default_x)
        default_x += 50


def end_race(x_cor):
    if x_cor >= 200:
        return False
    else:
        return True


def check_winner(bet, win_turtle):
    if bet == win_turtle:
        print(f"The {win_turtle} won the race! You win the bet!")
    else:
        print(f"The {win_turtle} won the race! You loose the bet!")


screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Track")
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Choose a color to bet on: ").lower()

turtle_list = []
color_list = ["red", "blue", "orange", "purple", "pink", "yellow", "green"]

set_up()
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if is_race_on:
            move_dist = random.randint(0, 10)
            turtle.forward(move_dist)
            x_pos = turtle.xcor()
            is_race_on = end_race(x_pos)

            if not is_race_on:
                winner_color = turtle.pencolor()
                turtle.write(arg="I won! ", font=('Arial', 14, 'bold'), align="right")
                check_winner(user_bet, winner_color)

screen.exitonclick()
