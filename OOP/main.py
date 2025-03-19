from pets import Pet, Food
from time import sleep
from colours import *

def pets():

    '''Args: name, species, description, age, colour'''

    pet1 = Pet("Garfield", "Cat", "Lazy cat", 5, "Orange")
    pet2 = Pet("Roach", "Horse", "TW3 Goat", 10, "Brown")
    pet3 = Pet("Scooby-Doo", "Dog", "Mystery solver", 7, "Brown")

    print(get_next_colour() + pet1.get_whole_description()) ; sleep(0.25)
    print(get_next_colour() + "\n" + pet2.get_whole_description()) ; sleep(0.25)
    print(get_next_colour() + "\n" + pet3.get_whole_description()) ; sleep(0.25)

def food():

    '''Args: name, food, price'''

    food1 = Food("Garfield", "Lasaña", 100)
    food2 = Food("Roach", "Carrot", 25)
    food3 = Food("Scooby-Doo", "Scooby Snacks", 50)

    print(get_next_colour() + "\n" + food1.get_whole_description()) ; sleep(0.25)
    print(get_next_colour() + "\n" + food2.get_whole_description()) ; sleep(0.25)
    print(get_next_colour() + "\n" + food3.get_whole_description()) ; sleep(0.25)

if __name__ == "__main__":
    pets()
    food()