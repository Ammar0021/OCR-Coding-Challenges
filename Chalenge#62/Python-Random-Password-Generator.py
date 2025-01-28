# Have the programme create random strong passwords mixing upper and lower case, symbols and numbers
# Have the password also use ASCII characters
# Have the passwords stored in an external file

#PYTHON

import random  
import string  
import os

def pass_generator():
    UPPER = string.ascii_uppercase  
    LOWER = string.ascii_lowercase  
    DIGITS = string.digits  
    SYMBOLS = string.punctuation

    every_char = UPPER + LOWER + DIGITS + SYMBOLS
    
    password_length = int(input("How many characters do you want your password to be?: ").strip())
    password = "".join(random.choice(every_char) for i in range(password_length))

    print("Your generated password is:", password) 
    folder_name = "Chalenge#62"  
    
    file_path = os.path.join(folder_name, "PasswordStorage.txt")
    
    # Opens the file in Append mode  
    with open(file_path, "a") as file:  
        file.write(password + "\n")
    
    print(f"Your password has been saved in '{file_path}'")
    return password 

while True:
    pass_generator()

    again = input("Do you want to generate another password? (y/n): ").strip().lower()
    if again == "n":
        break 
    elif again == "y":
        continue 
    else:
        print("Enter 'y' or 'n' only")