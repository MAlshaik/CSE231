import csv
from operator import itemgetter
from tkinter.tix import ROW

from numpy import disp

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    '''Prompts user to enter a file name and checks if it is valid'''
    file = input("Input data to open: ") + ".csv"
    #adds .csv to the input
    while(True):
        try:
            data = open(file)
            break
        except:
             print('\nError: file not found.  Please try again.')
             file = input('Enter a file name: ') + ".csv"
             #makes sure the csv file is valid
    return data
    
    

def read_file(fp):
    '''Reads the csv file and makes a list of touples for each character'''
    char_list = []
    fp.readline()
    for line in fp.readlines():
        line = line.strip().split(',')
        if line[-1] == '': line[-1] = ('None')
        
        tup = (line[0], line[2], line[3], int(line[1]), line[4])
        char_list.append(tuple(tup))
    return char_list


def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''Retrieves the characters that match a certain criteria'''
    pass
        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''Retrieves the characters that match all criteria'''
    pass

def get_region_list  (master_list):
    '''Retrieve all regions into a sorted non duplicate list'''
    sorted_list = []
    for tup in master_list:
        if tup[-1] == '': sorted_list.append('None')
        else: sorted_list.append(tup[-1])

    return sorted(set(sorted_list))
    

def sort_characters (list_of_tuples):
    '''Returns a list of characters sorted by rarity and name'''
    pass

def display_characters (list_of_tuples):
    '''Given a list of characters, display their information'''
    
    print(HEADER_FORMAT.format('Character', 'Element', 'Weapon','Rarity', 'Region'))
    for tup in list_of_tuples:
        print(ROW_FORMAT.format(tup[0], tup[1], tup[2], tup[3], tup[4]))

def get_option():
    '''Display a menu of options and prompt for input'''
    pass  
  
def main():
    file = open_file()
    master_list = read_file(file)
    print(get_region_list(master_list))
    display_characters(master_list)

if __name__ == "__main__":
    main()
    
