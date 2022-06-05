###########################################################

    #  Computer Project #3

    #

    #  Algorithm

    #    prompt for a file name

    #    input file name

    #    make sure file name is real (if not then reprompt)

    #    create a function that finds the min percent value when given a secific line

    #    the function the goes through the line and finds the min value using string slicing  

    #    make a similar function for the max percent value 

    #    make a function that finds the corrisponding GDP value to a percent GDP change value given a line number and an index for the GDP change value

    #    make a display function that turns the gdp values to trillions and displayes all the values in a specific format 

    #    make a main function that calls are the other functions
    

    ###########################################################



FILE = ''
#set a global variable for the file so that i do not need to call 
#open file and ask for a file name every function

def open_file():
#this function checks for a exesting file name then sets that file to the global variable FILE
#if the file name entered is not real then it prompts the user to enter an exesting file 
    global FILE 
    fileName = input("Enter a file name: ")
    while(True):
        try: 
            FILE =  open(fileName, 'r')
            return FILE
        except:
            print("Error. Please try again")
            fileName = input("Enter a FILE name: ")
    
def find_min_percent(line):
#this function moves through a specific line number entered and, using string slicing, 
#it finds the minimum percent change in GDP 
    global FILE 
    FILE.seek(0)
    row = FILE.readlines()[int(line)-1]
    min = 9999999
    rowVal = 76
    for i in range(47):
        i += 1
        columnVal = 76 + 12*i
        value = float(row[rowVal: columnVal].replace(' ', ''))
        #here i realiesed that rowVal cannot be a constant like 76 because otherwise it will combine 
        #two diffrent values and cause a 'string cannot be converted to float error'
        #to solve this i made rowVal = to the previouse value of columnVal
        if (value < min):
            min = value
            min_index = rowVal + 4
        rowVal = columnVal
    return min, min_index

def find_max_percent(line):
#this function moves through a specific line number entered and, using string slicing, 
#it finds the mmaximum percent change in GDP 
    global FILE 
    FILE.seek(0)
    row = FILE.readlines()[int(line)-1]
    max = -9999999
    rowVal = 76
    for i in range(47):
        i += 1
        columnVal = 76 + 12*i
        value = float(row[rowVal: columnVal].replace(' ', ''))
        if (value > max):
            max = value
            max_index = rowVal + 4
        rowVal = columnVal
    return max, max_index

def find_gdp(line, index):
#this function goes to the entered line and index then finds the corrisponding GDP value and returns it 
    global FILE 
    FILE.seek(0)
    row = FILE.readlines()[(43 - int(line)) + int(line)]
    gdp = float(row[index-4: index+6].replace(' ', ''))
    return gdp


        
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
#this function displays all value with a specific format 
    print("\nGross Domestic Product")
    print("min/max     change  year    GDP(trillions)")
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", min_val, min_year, min_val_gdp*0.001))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min", max_val, max_year, max_val_gdp*0.001))
def main():
#this is the main function where all the other functions are called 
    global FILE 
    open_file()
    FILE.seek(0)
    #since i was using a global variable for the FILE i had to repetedly use seek throughout the code 
    #so that the index would not go out of range

    min_val = find_min_percent('9')[0]
    min_val_index = find_min_percent('9')[1]
    max_val = find_max_percent('9')[0]
    max_val_index = find_max_percent('9')[1]

    FILE.seek(0)
    
    min_val_year = int(FILE.readlines()[7][min_val_index-4: min_val_index+8].replace(' ', ''))
    FILE.seek(0)
    max_val_year = int(FILE.readlines()[7][max_val_index-4: max_val_index+8].replace(' ', ''))

    min_val_gdp = find_gdp('9', min_val_index)
    max_val_gdp = find_gdp('9', max_val_index)

    display(min_val, min_val_year, min_val_gdp, max_val, max_val_year, max_val_gdp)

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()