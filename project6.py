import csv
from operator import itemgetter
from tkinter.tix import ROW

from numpy import disp
from operator import itemgetter

from sympy import li

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
        if line[-1] == '': line[-1] = None
        
        tup = (line[0], line[2], line[3], int(line[1]), line[4])
        char_list.append(tuple(tup))
    return char_list


def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''Retrieves the characters that match a certain criteria'''
    search_list = []
    for tup in list_of_tuples:
        if tup[criteria] != None:
            try:
                if tup[criteria].lower() == value.lower():
                    search_list.append(tup)
            except:
                if tup[criteria] == value:
                    search_list.append(tup)
                
    return search_list

        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''Retrieves the characters that match all criteria'''
    search_list = get_characters_by_criterion(master_list, 1, element)
    search_list = get_characters_by_criterion(search_list, 2, weapon)
    search_list = get_characters_by_criterion(search_list, 3, rarity)
    return search_list


def get_region_list (master_list):
    '''Retrieve all regions into a sorted non duplicate list'''
    if len(master_list) == 0: return []

    sorted_list = []
    for tup in master_list:
        if tup[-1] == '': sorted_list.append(None)
        else: sorted_list.append(tup[-1])

    sorted_list = set(sorted_list)

    if None in sorted_list: 
        sorted_list.remove(None)
        sorted_list = sorted(sorted_list)
    else:
        sorted_list = sorted(sorted_list)

    if len(sorted_list) == 1 and sorted_list[0] == None:
        return []

    return sorted_list
    

def sort_characters (list_of_tuples):
    '''Returns a list of characters sorted by rarity and name'''
    return sorted(sorted(list_of_tuples), key=itemgetter(3), reverse = True)

def display_characters (list_of_tuples):
    '''Given a list of characters, display their information'''
    
    print(HEADER_FORMAT.format('Character', 'Element', 'Weapon','Rarity', 'Region'))
    for tup in list_of_tuples:
        print(ROW_FORMAT.format(tup[0], tup[1], tup[2], tup[3], tup[4]))

def get_option():
    '''Display a menu of options and prompt for input'''
    try:
        option = int(input(MENU))
    except:
        print(INVALID_INPUT)
    if(option <= 1 or option >= 4):
        print(INVALID_INPUT)  
  
def main():
    file = open_file()
    master_list = read_file(file)
    print(master_list)
    display_characters(master_list)

if __name__ == "__main__":
    main()
    
