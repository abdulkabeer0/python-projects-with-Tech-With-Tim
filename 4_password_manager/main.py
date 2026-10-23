master_pwd = input("Enter your Master Password: ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add) press q to quit: ").lower()
    if mode == "q" or mode == "quit":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode")  
        continue