import turtle
import pandas

# TODO: 1. Convert the guess to Title case
# TODO: 2. Check if the guess is among the 50 states
# TODO: 3. Write a correct guesses onto the map
# TODO: 4. Use a loop to allow the user to keep guessing
# TODO: 5. Record the correct guesses in a list
# TODO: 6. Keep track of the score

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
is_game_over = True


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:                  Shorter List Comprehension :)
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


    # If answer_state is one of the states in all the states of the 50_states.csv
         #If they got it right:
            #Create a turtle to write the name of the state at the state's X and Y coordinates
#Save the missing states to states_to_learn.csv (create a new file)







