import random
from secrets import choice


def the_game():
    choices = ['paper', 'rock', 'scissors']
    player_choice = input("rock, paper or scissors?").lower()
    computer_choice = random.choice(choices)

    while player_choice not in choices:
        player_choice = input(
            "Please enter either rock, paper or scissors. (In the exact same way)").lower()

    print("Computer's choice is :" + computer_choice)
    print("Player's choice is:" + player_choice)


    if player_choice == computer_choice:
        print("tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("rock wins scissors. Well played!")
        elif computer_choice == "paper":
            print("paper wins rock. Better luck next time!")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("rock wins scissors. Better luck next time!")
        elif computer_choice == "paper":
            print("scissors wins paper. Well played!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Sissors wins paper. Better luck next time!")
        elif computer_choice == "rock":
            print("paper wins rock. Well Played!")

the_game()
answer = input("Would you like to play again? \n Type yes to play again and anything else to exit :)").lower()
while answer == "yes":
    the_game()
    answer = input("Would you like to play again? \n Type yes to play again and anything else to exit :)").lower()
print("See ya! Until next time buddy :).")