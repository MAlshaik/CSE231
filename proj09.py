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
    
def open_file():
    '''This function prompts the user to input a file name to open and keeps prompting until a correct name is entered. '''
    file1 = input("\nEnter the price's filename: ")
    file2 = input("\nEnter the security's filename: ")

    while(True):
        try: data1 = open(file1)
        except:
             print("\nFile not found. Please try again.")
             file = input("\nEnter the price's filename: ") 
             #makes sure the file is valid
        try: data2 = open(file2) 
        except:
             print("\nFile not found. Please try again.")
             file = input("\nEnter the security's filename: ") 
             #makes sure the file is valid
        
        if data1 != None and data2 != None:
            break

    return data1, data2

def read_file(securities_fp):
    '''Docstring'''
    master_dict = {}
    securities_fp.readline()
    names = set()

    for line in  csv.reader(securities_fp, quotechar='"', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True):
        names.add(line[1])
        master_dict[line[0]] = [line[1], line[3], line[4], line[5], line[6],[]] 
    
    return names, master_dict

        
def add_prices (master_dictionary, prices_file_pointer):
    '''Docstring'''
    prices_file_pointer.readline()
    for line in csv.reader(prices_file_pointer):
        try:
            master_dictionary[line[1]][5].append([line[0].strip(), float(line[2]), float(line[3]), float(line[4]), float(line[5])])
        except:
            continue

def get_max_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    tuples = []

    if company_symbol not in master_dictionary or len(master_dictionary[company_symbol][5]) == 0:
        return (None, None)

    for line in master_dictionary[company_symbol][5]:
        tuples.append((line[4],line[0]))
    
    return max(tuples)

def find_max_company_price (master_dictionary):
    '''Docstring'''
    pass

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''Docstring'''
    pass
            
def display_list (lst):  # "{:^35s}"
    '''Docstring'''
    pass
    
def main():
    pass
       
if __name__ == "__main__": 
    main() 
