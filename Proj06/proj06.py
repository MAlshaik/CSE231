###########################################################
#
#   Computer Project #6
#   Algorithm
#       Define all methods needed    
#       prompt for csv file until the name entered is valid
#       prompt user for option
#       if f the option requires further user input, then prompt user for the input
#       otherwise, print results
#       Ask for user input again until input is 4
#############################################################
import csv
from operator import itemgetter

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
    file = input("Enter file name: ") 
    #adds .csv to the input
    while(True):
        try:
            data = open(file)
            break
        except:
             print('\nError opening file. Please try again.')
             file = input('Enter file name: ') 
             #makes sure the csv file is valid
    return data
    
    

def read_file(fp):
    '''Reads the csv file and makes a list of touples for each character'''
    char_list = []
    fp.readline()
    for line in fp.readlines():
        line = line.strip().split(',')
        #strips the line from whitespace and splits the line into list indexes where ',' occurs
        if line[-1] == '': line[-1] = None
        
        tup = (line[0], line[2], line[3], int(line[1]), line[4])
        #orders tuple in desired way
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
            #makes sure that this doesnt raise an error if criteria is not a string
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
    sorted_list = []
    for tup in master_list:
        if tup[-1] == '': sorted_list.append(None)
        #if the region index is empty it turns it to None
        else: sorted_list.append(tup[-1])

    sorted_list = set(sorted_list)

    if None in sorted_list: 
        sorted_list.remove(None)
        #removes none so that it does not raise a type error when sorting
        sorted_list = sorted(sorted_list)
    else:
        sorted_list = sorted(sorted_list)

    return sorted_list
    

def sort_characters (list_of_tuples):
    '''Returns a list of characters sorted by rarity and name'''
    return sorted(sorted(list_of_tuples), key=itemgetter(3), reverse = True)

def display_characters (list_of_tuples):
    '''Given a list of characters, display their information'''
    if len(list_of_tuples) == 0:
        print("\nNothing to print.")
    else:
        print(HEADER_FORMAT.format('Character', 'Element', 'Weapon','Rarity', 'Region'))
        for tup in list_of_tuples:
            list_tup = list(tup)
            if None in list_tup: 
                list_tup[list_tup.index(None)] = "N/A"
                # if there is a None in the tuple it turns it to 'N/A'
            print(ROW_FORMAT.format(list_tup[0], list_tup[1], list_tup[2], list_tup[3], list_tup[4]))

def get_option():
    '''Display a menu of options and prompt for input'''
    try:
        option = int(input(MENU))
        if(option < 1 or option > 4):
        #checks if option is between 1 and 4
            print(INVALID_INPUT)
        else:
            return option
    except:
        print(INVALID_INPUT)
      

def is_int(value):
    '''checks if value is an integer'''
    while True:
        try: 
            value = int(value) 
            return True
        except: 
            return False

def main():
    file = open_file()
    master_list = read_file(file)
    option = 0
    while option != 4:
        option = get_option()
        if option == 1:
            print("\nRegions:")
            print(", ".join(get_region_list(master_list)))
            continue

        elif option == 2:
            criteria = input(CRITERIA_INPUT)
            while not is_int(criteria) or (int(criteria) < 1 or int(criteria) >  4):
            #makes sure that criteria is a valid value
                print(INVALID_INPUT)
                criteria = int(input(CRITERIA_INPUT))
            criteria = int(criteria)

            value = input(VALUE_INPUT)
            if criteria == 3:
                while not is_int(value):
                    print(INVALID_INPUT)
                    value = (input(VALUE_INPUT))
                value = int(value)
            
            criterion_list = get_characters_by_criterion(master_list, criteria, value)
            criterion_list = sort_characters(criterion_list)
            display_characters(criterion_list)

            continue

        elif option == 3:
            element = input(ELEMENT_INPUT)
            weapon = input(WEAPON_INPUT)
            rarity = input(RARITY_INPUT)

            while not is_int(rarity):
            # repeats until rarity is a valid value
                print(INVALID_INPUT)
                rarity = input(RARITY_INPUT)
            rarity = int(rarity)

            criteria_list = get_characters_by_criteria(master_list, element, weapon, rarity)
            criteria_list = sort_characters(criteria_list)
            display_characters(criteria_list)
            continue 

        elif option == 4:
            quit()
if __name__ == "__main__":
    main()
    
