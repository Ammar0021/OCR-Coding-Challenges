'''Palindromes 
Write a program that checks if a string entered by the user is a palindrome. A palindrome is a word that reads the same forwards as backwards like “racecar”'''

#PYTHON

def check_palindrome():
    while True:
        check = input("Enter your string: ").strip().lower()
        if not check.isalpha():
            print("Enter letters only")
            continue

        normal_string = check
        reversed_string = "".join(reversed(normal_string))

        if normal_string == reversed_string:
            print(f"\nYour word {check} is a Palindrome!")
        else:
            print(f"\nYour word {check} is Not a Palindrome!")
        break
        

def play_again():
    while True:
        pa = input("\nPlay Again? y/n: ").strip().lower()
        if pa in ["y", "yes"]:
            return True
        elif pa in ["n", "no"]:
            return False
        else:
            print("Invalid response. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    while True:
        check_palindrome()
        if not play_again():
            break