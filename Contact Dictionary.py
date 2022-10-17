import os


def view():# view persons informations
    file_path = 'names data base.txt'
    if os.stat(file_path).st_size == 0:
        print('File is empty')
    else:
        with open("names data base.txt", "r") as f:
            for line in f.readlines():
                data = line
                print(data)

def add():# add new person information
    name = input('Name: ')
    pwd = input("Info: ")

    with open('names data base.txt', 'a') as f:
        f.write("{\""+name + "\":\"" + pwd+"\"}\n")

def delete():#delete persons informations
    with open('names data base.txt', 'w'):
        del()
while True:
    command = input(
        "Would you like to add a new name or view existing ones [view, add] and press q to quit? ").lower()
    if command == "q":
        quit()
    elif command == "view":
        view()
    elif command == "add":
        add()
    elif command == "delete":
        delete()
        print("file has been deleted")
    else:
        continue