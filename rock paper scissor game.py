import random


def computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

print(computer_choice())

def player_choice():
    choices = ["rock", "paper", "scissor"]
    while True:
        choice = input("please enter your choice:")
        if choice not in choices:
            print("this is wrong anser please use one of: paper, scissor, rock")
        else:
            return choice
            break


player_score = 0
computer_score = 0


while True:
    print("Welcome to the game!")
    print("To play enter number of round otherwise if you want to exit enter simply exit.")
    rounds = input("How many round do you want to play?")
    if rounds == "exit":
        break
    
    for i in range(int(rounds)):
        player = player_choice()
        print(player)
        computer = computer_choice()
        print(computer)

        if computer == "rock" and player == "rock":
            pass
        elif computer == "rock" and player == "paper":
            player_score += 1
        elif computer == "rock" and player == "scissor":
            computer_score += 1
        elif computer == "paper" and player == "paper":
            pass
        elif computer == "paper" and player == "rock":
            computer_score += 1
        elif computer == "paper" and player == "scissor":
            player_score += 1
        elif computer == "scissor" and player == "scissor":
            pass
        elif computer == "scissor" and player == "rock":
            player_score += 1
        elif computer == "scissor" and player == "paper":
            computer_score += 1
    print("player score:",player_score)
    print("computer score:", computer_score)


