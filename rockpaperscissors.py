import random
from secrets import choice


def the_game():
    choices = ['Paper', 'Rock', 'Scissors']
    player_choice = input("Rock, Paper or Scissors?")
    computer_choice = random.choice(choices)

    while player_choice not in choices:
        player_choice = input(
            "Please enter either Rock, Paper or Scissors. (In the exact same way)")

    print("Computer's choice is :" + computer_choice)
    print("Player's choice is:" + player_choice)


    if player_choice == computer_choice:
        print("tie!")
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("Rock wins Scissors. Well played!")
        elif computer_choice == "Paper":
            print("Paper wins Rock. Better luck next time!")
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("Rock wins Scissors. Better luck next time!")
        elif computer_choice == "Paper":
            print("Scissors wins Paper. Well played!")
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print("Sissors wins Paper. Better luck next time!")
        elif computer_choice == "Rock":
            print("Paper wins Rock. Well Played!")

the_game()
answer = input("Would you like to play again? \n Type yes to play again and anything else to exit :)")
while answer == "yes":
    the_game()
    answer = input("Would you like to play again? \n Type yes to play again and anything else to exit :)")
print("See ya! Until next time buddy :).")