import os

def clear_screen():
        os.system('clear')
clear_screen()

class Pet(object):
    def __init__(self, name, species, description, age, colour):
        self.name = name
        self.species = species
        self.description = description
        self.age = age
        self.colour = colour

    '''Getters'''
    def get_name(self):
        return self.name
    
    def get_species(self):
        return self.species
    
    def get_description(self):
        return self.description
    
    def get_age(self):
        return self.age
    
    def get_colour(self):
        return self.colour
    
    def get_whole_description(self):
        return f"{self.name} is a {self.species} and has colour {self.colour}, is {self.age} years old, knows as: {self.description}"
    
    '''Setters'''
    def set_name(self, name):
        self.name = name

    def set_species(self, species):
        self.species = species

    def set_description(self, description):
        self.description = description

    def set_age(self, age):
        self.age = age
    
    def set_colour(self, colour):
        self.colour = colour


class Food:
    def __init__(self, name, food, price):
        self.name = name
        self.food = food
        self.price = price

    '''Getters'''
    def get_name(self):
        return self.name
    
    def get_food(self):
        return self.food
    
    def get_price(self):
        return self.price
    
    def get_whole_description(self):
        return f"{self.name} has food {self.food} and costs {self.price}"
    
    '''Setters'''

    def set_name(self, name):
        self.name = name

    def set_food(self, food):
        self.food = food
    
    def set_price(self, price):
        self.price = price

