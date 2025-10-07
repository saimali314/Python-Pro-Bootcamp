from random import randint
from art import logo

level=""
number=0

# This is main function from where program start its execution.
def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    game_start()

# This is where level, correct number is to be decided.
def game_start():
    global level
    global number
    number= randint(1,100)
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (level=="easy"):
        game_easy()
    elif (level=="hard"):
        game_hard()
    else:
        print("Wrong input")

# This is for the functionality of game at easy level.
def game_easy():
    n=10
    while(n>0):
        print(f"You have {n} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if(guess>number):
            print("Too high")
            print("Guess again")
            n -= 1
        if(guess<number):
            print("Too low")
            print("Guess again")
            n -= 1
        if (guess == number):
            print(f"You got it! The answer is {guess}")
            break
    if (n==0):
        print("You are ranout of tries Try your luck later!")

# This is for the functionality of game of hard level.
def game_hard():
    n = 5
    while (n > 0):
        print(f"You have {n} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if (guess > number):
            print("Too high")
            print("Guess again")
            n -= 1
        if (guess < number):
            print("Too low")
            print("Guess again")
            n -= 1
        if (guess == number):
            print(f"You got it! The answer is {guess}")
            break
    if (n == 0):
        print("You are ranout of tries Try your luck later!")


main()