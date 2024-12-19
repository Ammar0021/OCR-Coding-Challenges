# Have the programme create random strong passwords mixing upper and lower case, symbols and numbers
# Have the password also use ASCII characters
# Have the passwords stored in an external file

#PYTHON

import random  
import string

def pass_generator():
    UPPER = string.ascii_uppercase  
    LOWER = string.ascii_lowercase  
    DIGITS = string.digits  
    SYMBOLS = string.punctuation

    every_char = UPPER + LOWER + DIGITS + SYMBOLS
    
    password_length = int(input("How many characters do you want your password to be?: ").strip())
    password = "".join(random.choice(every_char) for i in range(password_length))

    print("Your generated password is:", password)
    with open("PasswordStorage.txt", "a") as file:  
        file.write(password + "\n")
    
    print("Your password has been saved in 'PasswordStorage.txt'")
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
