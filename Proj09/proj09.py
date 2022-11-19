###########################################################
#   Computer Project #9
#   Algorithm
#       Define all methods needed    
#       prompt for prices, and securities files until valid values are entered
#       print menue
#       prompt user for option 1-6
#       depending on option, call required functions
#       ask for user for input if needed
#       print results
#       Ask for user input again until input is 6
#############################################################
import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
TITLE = "Companies in the New York Stock Market from 2010 to 2016"
    
def open_file():
    '''This function prompts the user to input a file name to open and keeps prompting until a correct name is entered. '''
    file1 = input("\nEnter the price's filename: ")
    file2 = input("\nEnter the security's filename: ")

    while(True):
        try: 
            data1 = open(file1)
        except:
             print("\nFile not found. Please try again.")
             file = input("\nEnter the price's filename: ") 
             #makes sure the file is valid
        try: 
            data2 = open(file2) 
        except:
             print("\nFile not found. Please try again.")
             file = input("\nEnter the security's filename: ") 
             #makes sure the file is valid
        try:
            if data1 != None and data2 != None:
                break
        except:
            continue

    return data1, data2

def read_file(securities_fp):
    '''This function takes the security’s file pointer that has the names of the companies and their codes.'''
    master_dict = {}
    securities_fp.readline()
    names = set()

    for line in  csv.reader(securities_fp, quotechar='"', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True):
        names.add(line[1])
        master_dict[line[0]] = [line[1], line[3], line[4], line[5], line[6],[]] 
        #adds the required elements to the master_dict in the correct order
    
    return names, master_dict

        
def add_prices (master_dictionary, prices_file_pointer):
    '''This funciton adds the reads the prices file and adds prices to the master_dictionary'''
    prices_file_pointer.readline()
    for line in csv.reader(prices_file_pointer):
        try:
            master_dictionary[line[1]][5].append([line[0].strip(), float(line[2]), float(line[3]), float(line[4]), float(line[5])])
            #appends the prices to the list in the last index of each dictionary iteam.
        except:
            continue

def get_max_price_of_company(master_dictionary, company_symbol):
    '''This function takes the master dictionary and a company symbol, and it gets the max high price and the date of the max price.'''
    tuples = []

    if company_symbol not in master_dictionary or len(master_dictionary[company_symbol][5]) == 0:
        return (None, None)
        # if the company symbol doesnt exist or the company doesnt have prices return None

    for line in master_dictionary[company_symbol][5]:
        tuples.append((line[4],line[0]))
        #appends (price, name)
    
    return max(tuples)

def find_max_company_price(master_dictionary):
    '''This function takes the master dictionary and finds the company with the highest high price.'''
    tuples = []
    for company in master_dictionary:
        tuples.append((get_max_price_of_company(master_dictionary, company)[0], company))
    
    tuples = [i for i in tuples if None not in i]
    #gets rid of all none values
    maxi = max(tuples)
    return (maxi[1], maxi[0])
    

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''This function uses the master dictionary and company symbol to find the average high price for the company.'''
    if company_symbol not in master_dictionary or len(master_dictionary[company_symbol][5]) == 0:
        return 0.0
    
    prices = [line[4] for line in master_dictionary[company_symbol][5]]
    #makes a list of prices

    return round(sum(prices)/len(prices),2)
    
    

            
def display_list (lst):  # "{:^35s}"
    '''This function takes a list of strings and displays that list in three columns, each column is 35 characters wide.'''
    count = 0
    for i in lst:
        if count < 2:
            print(f"{i:^35s}", end="")
            count += 1
        elif count == 2:
            print(f"{i:^35s}")
            count = 0
    
def main():
    print(WELCOME)
    file1, file2 = open_file()
    names, master_dictionary = read_file(file2)
    add_prices(master_dictionary, file1)
    option = 0

    while option != 6:
        print(MENU)
        option = int(input("\nOption: "))
        if option == 1:
            print(f"\n{TITLE:^105s}")
            display_list(list(sorted(names)))
            print("\n")
        if option == 2:
            symboles = [i for i in master_dictionary]
            print("\ncompanies' symbols:")
            display_list(sorted(symboles))
            print("\n")
        if option == 3:
            symbole = input("\nEnter company symbol for max price: ")

            while symbole not in master_dictionary:
                print("\nError: not a company symbol. Please try again.")
                symbole = input("\nEnter company symbol for max price: ")
            max_tuple = get_max_price_of_company(master_dictionary, symbole)

            if max_tuple == (None, None):
                print("\nThere were no prices.")
            else:
                print(f"\nThe maximum stock price was ${max_tuple[0]:.2f} on the date {max_tuple[1]:s}/\n")
        if option == 4:
            max_price = find_max_company_price(master_dictionary)
            print(f"\nThe company with the highest stock price is {max_price[0]:s} with a value of ${max_price[1]:.2f}\n")
        if option == 5:
            symbole = input("\nEnter company symbol for average price: ")

            while symbole not in master_dictionary:
                print("\nError: not a company symbol. Please try again.")
                symbole = input("\nEnter company symbol for average price: ")
            
            avg_price = get_avg_price_of_company(master_dictionary, symbole)
            if avg_price == 0.0:
                print("\nThere were no prices.")
            else:
                print(f"\nThe average stock price was ${avg_price:.2f}.\n")
        if option == 6:
            quit()
        
       
if __name__ == "__main__": 
    main()
