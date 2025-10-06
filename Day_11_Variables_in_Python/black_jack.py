import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []
computer = []
user_score = 0
computer_score = 0
new_card = 0
new_compcard = 0
first_round= True
final_round= False

def random_card():
    global user
    global computer
    if (first_round == True):
        user = random.sample(cards,2)
        computer = random.sample(cards,2)
        calculate_score()

def random_computer_card():
    global computer
    global final_round
    global new_compcard
    if(computer_score < 17):
        new_compcard = random.choice(cards)
        computer.append(new_compcard)
        final_round = True
        calculate_score()
    elif(computer_score >= 17):
        final_round=True
        if (computer_score > 21):
            print(f"You final hand: {user}, final score: {user_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            print("You won!")
            main()
            quit()
        else:
            if (user_score > computer_score):
                print(f"You final hand: {user}, final score: {user_score}")
                print(f"Computer's final hand: {computer}, final score: {computer_score}")
                print("You won!")
                main()
                quit()
            elif (user_score == computer_score):
                print(f"You final hand: {user}, final score: {user_score}")
                print(f"Computer's final hand: {computer}, final score: {computer_score}")
                print("Game Draws!")
                main()
                quit()
            else:
                print(f"You final hand: {user}, final score: {user_score}")
                print(f"Computer's final hand: {computer}, final score: {computer_score}")
                print("You lose!")
                main()
                quit()


def calculate_score():
    global user_score
    global computer_score
    global new_card
    global new_compcard
    global first_round
    if (first_round == True):
            for card in user:
                user_score += card
            for card in computer:
                computer_score += card
            check_blackjack()
            first_round = False
    elif (final_round == False):
        user_score += new_card
        computer_score += new_compcard
        new_card=0
        new_compcard=0
    elif (final_round == True):
        computer_score += new_compcard
        new_compcard = 0


    if (final_round == False):
        print(f"You cards: {user}, current score: {user_score}")

    check_scorelimit()

def check_blackjack():
    if 11 in user:
        if 10 in user:
            print(f"You final hand: {user}, final score: {user_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            print("You have a blackjack, You Won!")
            main()
            quit()
    if 11 in computer:
        if 10 in computer:
            print(f"You final hand: {user}, final score: {user_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            print("Your Opponent have blackjack, You lose!")
            main()
            quit()


def check_scorelimit():
    global user_score
    global user
    if (user_score > 21):
        if 11 in user:
            user_score -= 11
            user.remove(11)
            user_score += 1
            user.append(1)
            print(f"You new cards: {user}, current score: {user_score}")
            check_scorelimit()
        else:
            print(f"You final hand: {user}, final score: {user_score}")
            print(f"Computer's final hand: {computer}, final score: {computer_score}")
            print("You went over, You lose!")
            main()
            quit()

    else:
        if (final_round == False):
            another_card()
        if (final_round == True):
            random_computer_card()

def another_card():
    global user
    global new_card
    global final_round
    decision= input("Type 'y' to get another card, type 'n' to pass: ")
    if (decision == 'y'):
        new_card= random.choice(cards)
        user.append(new_card)
        calculate_score()
    if (decision == 'n'):
        final_round = True
        random_computer_card()

def reset_globals():
    global user, computer, user_score, computer_score
    global new_card, new_compcard, first_round, final_round

    user = []
    computer = []
    user_score = 0
    computer_score = 0
    new_card = 0
    new_compcard = 0
    first_round = True
    final_round = False

def main():
    reset_globals()
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == "y":
        print(logo)
        random_card()
    else:
        print("Thank you for playing!")


main()