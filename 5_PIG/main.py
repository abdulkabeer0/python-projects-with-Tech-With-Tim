import random

user_current_score = 0
computer_current_score = 0

print("Welcome to Luck Game!")

choice = input("Do you want to play Luck Game: ").lower()
if choice != "yes":
    quit()

target_score = input("Enter a Target Score: ")
if target_score.isdigit():
    target_score = int(target_score)
else:
    print("Invalid Syntax! | Enter a Valid number next time")
    quit()

y_counter = []
while True:   
    user_turn = input("Enter Y for your turn and C for computer turn: ").lower()

    if user_turn != "c" and user_turn != "y":
        print("Invalid Syntax\n")
        continue

    elif len(y_counter) == 1 and user_turn != "c":
        print("Limit Crossed")
        user_turn = "c"
        
    if user_turn == "y":
        y_counter += user_turn
        user_score = random.randint(1,6)

        if user_score > 1:
            user_current_score += user_score
            print("You got",user_score,"points\nYour currect points are",user_current_score,"\n")           
            user_score = 0

            if user_current_score >= target_score:
                print("You won by achiveing",user_current_score,"Points")
                break
        else:
            user_current_score = 0
            print("Opps! Your current score is now",user_current_score,"\n")

    elif user_turn == "c": 
        y_counter = []    
        computer_score = random.randint(1,6)

        if computer_score > 1:
            computer_current_score += computer_score
            print("Computer got",computer_score,"points\nComputer current points are",computer_current_score,"\n")
            computer_score = 0

            if computer_current_score >= target_score:
                print("Computer won by achiveing",computer_current_score,"Points")
                break
        else:
            computer_current_score = 0
            print("Opps Computer points are now",computer_current_score,"\n")       
        