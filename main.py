import pyfiglet
import random
import signal
from os import system
from game_data import data
import helper

def handler(signum, frame):
    system("cls")
    exit(1)

signal.signal(signal.SIGINT, handler)

def start_game():
    print("Welcome to the Higher Lower Game!")
    play_again = True
    while play_again:
        play_again = play_game()
        system("cls")
    system("cls")

def play_game():
    print(pyfiglet.figlet_format("Higher Lower"))
    score = 0
    wrong_choice = False
    while not wrong_choice:
        random_figures = random.sample(data, 2)
        helper.print_compare(random_figures[0], random_figures[1])
        winner = max(random_figures, key=lambda x: x["follower_count"])
        correct_choice = 'A' if random_figures[0] == winner else 'B'
        user_choice = helper.validate_user_input_compare(input("Who has more followers on Instagram? A/B: "))
        if user_choice == correct_choice:
            score += 1
            print(f"Correct! Current score: {score}")
        else:
            wrong_choice = True
            print(f"Wrong choice. Final score: {score}")
    return helper.validate_user_input_play_again(input("Do you want to play again? (y/n): ")) == 'y'

start_game()
