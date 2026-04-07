#Rock Paper Scissors game
import random

def opnt_choice(): #Computer making choice
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    return computer

def game(): #Actual game
    user_score = 0
    comp_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    while rounds != 0:
        user_input = input("Enter your choice: ").capitalize() #Users choice
        comp_choice = opnt_choice()
        print(comp_choice)
        if user_input == comp_choice:#Special case
            pass
        elif user_input == "Rock":
            if comp_choice == "Paper":
                comp_score += 1
            elif comp_choice == "Scissors":
                user_score += 1
        elif user_input == "Paper":
            if comp_choice == "Rock":
                user_score += 1
            elif comp_choice == "Scissors":
                comp_score += 1
        elif user_input == "Scissors":
            if comp_choice == "Rock":
                comp_score += 1
            elif comp_choice == "Paper":
                user_score += 1
        else:
            print("Invalid object \n Try Again :(")
            game()
        rounds -= 1
    return user_score, comp_score

print("You have a choice of 'Rock', 'Paper' and 'Scissors")
(player, computer) = game()

if player < computer:
    print(f"{'Player' : < 10} : {player}\n{'Computer' : < 10} : {computer}")
    print("Sorry, You Lose")
elif player > computer:
    print(f"{'Player':  < 10} : {player}\n{'Computer' : < 10} : {computer}")
    print("Congrats, You Win")
elif player == computer:
    print(f"{'Player' : < 10} : {player}\n{'Computer' : < 10} : {computer}")
    print("OK, It is a tie")
else:
    pass