from art import logo
from art import vs
from game_data import data
from random import randint

start_game=True
finish_game=False
score=0
selection=""
value_a=0
value_b=0

# Here is the main game class which ask for values after displaying random two entities
def game():
    global selection
    global value_a
    global value_b
    data_size=len(data)
    value_a=randint(0, data_size-1)
    print(f"Compare A: {data[value_a]["name"]}, a {data[value_a]["description"]}, from {data[value_a]["country"]}.")
    print(vs)
    value_b = randint(0, data_size-1)
    print(f"Compare B: {data[value_b]["name"]}, a {data[value_b]["description"]}, from {data[value_b]["country"]}.")
    selection=input("Who has more followers? Type 'A' or 'B': ")
    print(selection)
    compare()

#Here is the main start point of my program where I checked the status of game whether it game is just started, either in running phase and then finished at some point.
def main_logic():
    global start_game
    global finish_game
    if start_game==True and finish_game==False:
        print(logo)
        start_game=False
        game()
    elif start_game == False and finish_game == False:
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score: {score}.")
        game()
    elif start_game == False and finish_game==True:
        print("\n" * 20)
        print(logo)
        print(f"Sorry that's wrong. Final Score: {score}.")


#This method basically compare the player selection and call main logic method either by adding score 1 if right otherwise simply calling it finish game and calling main logic method.
def compare():
    global finish_game
    global score
    if(selection == 'A'):
        if (data[value_a]['follower_count'] > data[value_b]['follower_count']):
            score += 1
            main_logic()
        else:
            finish_game=True
            main_logic()
    elif (selection == 'B'):
        if (data[value_b]['follower_count'] > data[value_a]['follower_count']):
            score += 1
            main_logic()
        else:
            finish_game = True
            main_logic()
