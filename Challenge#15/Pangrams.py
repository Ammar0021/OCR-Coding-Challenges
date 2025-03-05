#Pangrams 
#”The quick brown fox jumps over the lazy dog”; note how all 26 English-language letters are used in the sentence.
#Your goal is to implement a program that takes a series of strings (one per line) and prints either True (the given string is a pangram), or False if it is not.

#PYTHON

def is_pangram(x):
    x = x.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in x:
            return False
    return True

if __name__ == "__main__":
    while True:
        try:
            print("Type in a sentence: ", end="")
            line = input().strip()
            if line == "":
                break
            print(is_pangram(line))
        except EOFError:
            break