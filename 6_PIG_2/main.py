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
    
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to Roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:  
                print("You Rolled 1 Turn Done!")
                current_score = 0 
                break
            else:
                current_score += value
                print("You Rolled a:",value)

            print("Your current score is", current_score)

        players_scores[player_idx] += current_score
        print("Your current score is:",players_scores[player_idx])