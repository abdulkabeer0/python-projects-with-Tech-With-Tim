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
        # if players <= 2 or players >= 4:
        if players >= 2 and players <= 4:
            break
        else: