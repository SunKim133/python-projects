import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
bg_image = 'blank_states_img.gif'
screen.addshape(bg_image)

game_data = pd.read_csv('50_states.csv')
states_list = game_data.state.to_list()
turtle.shape(bg_image)

score = 0
guesses = []

while score < 50:
    user_answer = screen.textinput(title=f'{score}/50 States Correct',
                                   prompt="What's the next state name?").title()
    if user_answer == 'Exit':
        states_to_learn = []
        for state in states_list:
            if state not in guesses:
                states_to_learn.append(state)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn.csv')
        break
    if user_answer in states_list:
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        state_data = game_data[game_data.state == user_answer]
        label.goto(x=int(state_data.x), y=int(state_data.y))
        label.write(state_data.state.item(), align='center', font=('Arial', 10, 'normal'))
        score += 1
        guesses.append(user_answer)

screen.exitonclick()