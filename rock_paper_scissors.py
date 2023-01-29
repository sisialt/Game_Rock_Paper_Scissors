import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
computer_move = ""
computer_random = random.randint(1, 3)

if player_move == "r" or player_move == "rock" or player_move == "Rock" or player_move == "ROCK":
    player_move = rock
elif player_move == "p" or player_move == "paper" or player_move == "Paper" or player_move == "PAPER":
    player_move = paper
elif player_move == "s" or player_move == "scissors" or player_move == "Scissors" or player_move == "SCISSORS":
    player_move = scissors
else:
    raise SystemExit("Invalid input... Try again! ;)")

if computer_random == 1:
    computer_move = rock
elif computer_random == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if player_move == rock and computer_move == scissors:
    print("You won!!! :) Rock beats scissors. Let`s play again!")
elif player_move == paper and computer_move == rock:
    print("You won!!! :) Paper beats rock. Let`s play again!")
elif player_move == scissors and computer_move == paper:
    print("You won!!! :) Scissors beats paper. Let`s play again!")
elif player_move == computer_move:
    print("Draw... Let`s play again!")
elif computer_move == rock and player_move == scissors:
    print("You lost... :( The scissors get broken by the rock. But let`s play again!")
elif computer_move == paper and player_move == rock:
    print("You lost... :( The rock is covered by the paper. But let`s play again!")
else:
    print("You lost... :( The paper gets cut by the scissors. But let`s play again!")
