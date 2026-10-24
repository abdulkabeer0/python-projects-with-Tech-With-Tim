from cryptography.fernet import Fernet

# def write_key(): This function should be used once to create a single key, if one key is generated in key.key file no need to call this function again.
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

# write_key() # Use this function once to generate key in key.key file. once generated no need to call this function again.

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your Master Password: ")

key = load_key() + master_pwd.encode() # in this key variable we are having raw key located in key.key file and we are concatinating with our master password coverted in bytes. This is done So only correct passwords can shown only when master password in entered correctly.
fer = Fernet(key) # Contains cryptography with master password which can be used to encrypt and decrypt passwords.

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("user: " + user + " | " + "passwd: " + fer.decrypt(passwd.encode()).decode()) # this is used to decrypt passwords so we can view them correctly.

def add():
    name = input("Enter your Username Name: ")
    pwd = input("Enter your password: ")

    with open("password.txt","a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n") # In this we are encrypting passwords so they can be shown in scramble aplhabets in password file

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