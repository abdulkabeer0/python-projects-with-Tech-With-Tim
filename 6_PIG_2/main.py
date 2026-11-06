import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enters Number of Player (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print("Minimum 2 and Maximum 4 Players can Play!\n")
    else:
        print("Enter a Valid Number!\n")

max_score  = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    current_score = 0

    should_roll = input("Would you like to Roll (y)? ")
    if should_roll.lower() != "y":
        break
    
    value = roll()
    if value == 1:
        print("You Rolled 1 Turn Done!")
        break
    else:
        current_score += value
        print("You Rolled a:",value)

    print("Your current score is", current_score)