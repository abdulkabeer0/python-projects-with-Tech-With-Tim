from cryptography.fernet import Fernet

master_pwd = input("Enter your Master Password: ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("user: " + user + " | " + " passwd:" + passwd)

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