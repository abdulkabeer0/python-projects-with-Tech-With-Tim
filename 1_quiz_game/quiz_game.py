print("Welcome to my Computer Quiz")

playing = input("Do you want to Play? ").lower()

if playing != "yes":
    quit()

print("Okay! Lets Play :)")

answer = input("What does N word means? ").lower()
if answer == "nigga" or answer == "nigger":
    print("Correct! Welcome to Racism community")
else:
    print("Incorrect! You Lost in game but Won in Life")


answer = input("\nWho was the Best Hero in the History?\nHint: He failed as an Art student? ").lower()
if answer == "adolf hitler" or answer == "hitler" or answer == "austrian painter":
    print("Correct! Welcome to Reality")
elif answer == "adolf":
    print("Incorrect! You wouldnt be charged to write a full Legendary Name")
else:
    print("Incorrect! You gotta need some history lessons dude")


answer = input("\nIf 2 black people riding in a Car so whos Driving? ").lower()
if answer == "police" or answer == "cops" or answer == "cop": 
    print("Correct! An IQ too high")
else:
    print("Incorrect! You have a hidden talent Keep it hidden")


answer = input("\nThe greatest Genosider in the World? ").lower()
if answer == "israel" or answer == "netanyahu" or answer == "benjamin netanhayu":
    print("Correct! You hit the Reality ")
else:
    print("Incorrect! Definitely you are a Juice")


answer = input("\nName a body Organ that starts with letter D? ").lower()
if answer in ("duodenum", "dermis", "diaphragm", "diencephalon", "descending colon", "dura mater", "decidua", "duas layer"):
    print("Correct! Definitely i know what comes in your mind first")
elif answer == "dick":
    print("Correct! but there were more options as well (U need to hesitate Dude)")
else:
    print("Incorrect! from now onwards read biology daily (read Reproduction chapter with focus) ")