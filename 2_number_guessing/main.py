import random

range_of_input = input("Enter a Number: ")

if range_of_input.isdigit():
    range_of_input = int(range_of_input)

    if range_of_input < 0:
        print("Enter a Number Greater than 0")
        quit()
else: 
    print("MF Enter a number next time! Understand")
    quit()

random_number = random.randint(0, range_of_input)

user_guesses = 0

while True:
    user_guess = input("Guess a Number: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        user_guesses += 1
    else:
        print('Enter a number next time')
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print("You are Above")
    else:
        print("You are Below")

print("You have taken",user_guesses,"gusses to guess Correct!")