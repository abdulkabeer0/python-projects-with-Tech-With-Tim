import random

print("Welcome to Rock Paper Scissor Game")
print("Enter q or quit to exit from the game.")

computer_wins = 0
user_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_weapon = input("\nEnter Your Weapon Rock/Paper/Scissor: ").lower()

    if user_weapon == "q" or user_weapon == "quit":
        break

    if user_weapon not in options:
        print("Enter correct Weapon Rock/Paper/Scissor")
        continue
    
    random_number = random.randint(0,2)
    computer_weapon = options[random_number]
    # 0: Rock, 1: Paper, 2: Scissor
    print("Computer weapon was",computer_weapon + ".")

    if user_weapon == "rock" and computer_weapon == "scissor":
        print("You Won!")
        user_wins += 1
    elif user_weapon == "paper" and computer_weapon == "rock":
        print("You Won!")
        user_wins += 1
    elif user_weapon == "scissor" and computer_weapon == "paper":
        print("You Won!")
        user_wins += 1
    elif user_weapon == computer_weapon:
        print("Tie")
    else:
        print("Computer Won")
        computer_wins += 1

print("You Won",user_wins,"Times")
print("Computer Won",computer_wins,"Times")
print("GoodBye!")