// Have the programme create random strong passwords mixing upper and lower case, symbols and numbers
// Have the password also use ASCII characters
// Have the passwords stored in an external file

// PSEUDOCODE

IMPORT random
IMPORT string

function pass_generator()
    UPPER = string.ascii_uppercase  
    LOWER = string.ascii_lowercase  
    DIGITS = string.digits  
    SYMBOLS = string.punctuation

    every_char = UPPER + LOWER + DIGITS + SYMBOLS

    password_length = input("How many characters do you want your password to be?")
    password = "".JOIN(RANDOM.CHOICE(every_char) for i = password_length))


    print("Your generated password is password is:, password)
    myFile = openWrite(PasswordStoage.txt)
    print("Your password has been saved in 'PasswordStorage.txt'")
    return password

while True:
    pass_generator()

    again = input(""Do you want to generate another password? (y/n)")
    if again == "y" then
        CONTINUE
    elif again == "n" then
        BREAK
    else
        print("Enter 'y' or 'n' only")
    endif

endfunction
    
    
    