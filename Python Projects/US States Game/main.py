import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(False)

data = pandas.read_csv("50_states.csv")
print(data)
states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("missed_states_csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        turtle.penup()
        turtle.hideturtle()
        state_data = data[data.state == answer_state]
        turtle.goto(int(state_data.x), (int(state_data.y)))
        turtle.write(answer_state)

