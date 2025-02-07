import os 

def clear():
    os.system("cls" if os.name == "nt" else "clear")
def main():
    clear()
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    form = input("Enter your form: ")
    info = (f"Your name is {name}, \nYou are {age} years old, \nYou are in form {form}\n")

    folder_name = "Challenge#61"
    file_path = os.path.join(folder_name, "user_info.txt")
 
    with open(file_path, "a") as storage_file:
        storage_file.write(info)
        print("Information appended to user_info.txt")

if __name__ == "__main__":
    main()