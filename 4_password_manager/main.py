master_pwd = input("Enter your Master Password: ")

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            print(line.rstrip()) # rstrip ends or cuts the extra line when viewing or reading the file.

def add():
    name = input("Enter your Account Name: ")
    pwd = input("Enter your password: ")

    with open("password.txt","a") as f:
        f.write(name + " | " + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add) press q to quit: ").lower()
    if mode == "q" or mode == "quit":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")  
        continue