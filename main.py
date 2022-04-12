import turtle
import pandas

screen = turtle.Screen()
screen.title(titlestring="U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess The State",
                                  prompt="What is the another state").capitalize()
    if user_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if user_state in all_states:
        guessed_states.append(user_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_state)

