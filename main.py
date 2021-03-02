from turtle import Screen, Turtle, textinput
import pandas as pd

# Declare initial variables
map_image_path = "./blank_states_img.gif"
states_data_path = "./50_states.csv"
states_correct = []


# Set-up screen
screen = Screen()
screen.setup(height=491, width=725)
screen.title("US States Game")
screen.bgpic(map_image_path)

# Set-up turtle for writing
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.pencolor('black')

# Load state data
states = pd.read_csv("50_states.csv")

game_is_on = True

while game_is_on:
    user_input = textinput(f"{len(states_correct)}/50 States Correct", "What's another state name?")
    if type(user_input) == str:
        user_input = user_input.title()  # Convert user input to title case to ease comparison with state data
        if states.state.str.contains(user_input).any():
            state_x = int(states[states.state == user_input].x)
            state_y = int(states[states.state == user_input].y)
            turtle.goto(state_x, state_y)
            turtle.write(user_input, align='center')
            states_correct.append(user_input)
        else:
            print(False)
    else:
        game_is_on = False  # If user clicks cancel or doesn't enter a name, the game loop ends

screen.exitonclick()
