import random


def computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)


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

print("Welcome to the game!")
print("please select one of these commands.")


command_help = "command list:\nrounds : enter how many rounds do you wanna play the game.\nexit : exit the programm"
print("\n\n"+command_help)


commands = ["exit", "rounds"]




while True:
    while True:
        operation = input("\n\ncommand:")
        
        if operation not in commands:
            print("\n\nplease enter one of command list operation.")
            print(command_help)
            
        elif operation == "rounds":
            break
        elif operation == "exit":
            break

    if operation == "exit":
        break
    elif operation == "rounds":
        rounds = input("please enter number of round do you want to play:")
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

    print("\n\nplayer score:",player_score)
    print("computer score:", computer_score)
