import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
score = 0

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
if answer_state in all_states:
    guessed_states.append(answer_state)
    score += 1

