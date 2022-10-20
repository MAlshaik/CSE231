import math
import pylab
from sqlalchemy import null

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
year = ''

def open_file():
    global year
    year_str = input("Enter a year where 1990 <= year <= 2015: ")
    while(True):
        try: 
            if(int(year_str) >= 1990 and int(year_str) <= 2015):
                year = int(year_str)
                FILE =  open(f"year{year_str}.txt", 'r')
                return FILE
        except:
            try:
                num = int(year_str)
            except:
                print("Error in year. Please try again.")
                year_str = input("Enter a year where 1990 <= year <= 2015: ")
            if((int(year_str) >= 1990 and int(year_str) <= 2015) == False):
                print("Error in year. Please try again.")
                year_str = input("Enter a year where 1990 <= year <= 2015: ")
            else:
                print(f"Error in file name: year{year_str}.txt")
                year_str = input("Enter a year where 1990 <= year <= 2015: ")
       
    
def read_file(fp):
    file_list = []
    next(fp)
    next(fp)
    for line in fp:
        line = line.replace('\t', ' ')
        split_line = line.split(' ')
        split_line = list(filter(None, split_line))
        new_filtered_list = []
        for i in split_line:
            i = i.replace('\n', '')
            new_filtered_list.append(i)
        file_list.append(new_filtered_list)
    
    return file_list
        
def find_average(data_lst):
    col6 = 0
    col4 = 0
    for list in data_lst:
        col6 += float(list[6].replace(',', ''))
        col4 += float(list[3].replace(',', ''))
    return col6/col4
    
def find_median(data_lst):
    med = 99999
    for list in data_lst:
        if (abs(50 - float(list[5])) < med):
            med = abs(50 - float(list[5]))
            med_list = list
    return float(med_list[7].replace(',', ''))
        
def get_range(data_lst, percent):
     for list in data_lst:
        if (float(list[5]) >= percent):
            return ((list[0], list[2]), list[5], list[7])
    

def get_percent(data_lst,salary):
    for list in data_lst:
        if (salary >= float(list[0].replace(',', '')) and salary <= float(list[2].replace(',', ''))):
            return ((list[0], list[2]), list[5])
    

def main():
    global year
    data = read_file(open_file())

    print("For the year {:4d}:".format(year))
    print("The average income was ${:<13,.2f}".format(find_average(data)))
    print("The median income was ${:<13,.2f}\n".format(find_median(data)))
    
   # response = input("Do you want to plot values (yes/no)? ")
    #if response.lower() == 'yes':
        # determine x_vals, a list of floats -- use the lowest 40 income ranges
        # determine y_vales, a list of floats of the same length as x_vals
        # do_plot(x_vals,y_vals,year)
    
    choice = input("Enter a choice to get (r)ange, (p), or nothing to stop: ")
    
    while choice:
        if (choice == 'r'):
            try:
                percent = input("Enter a percent: ")
                print(f'\n{float(percent)}% of incomes are below {get_range(data, float(percent))[0][0]}')
            except: 
                print("Error in percent. Please try again")
        elif (choice == 'p'):
            
            income = input("Enter an income: ")
            if(float(income) > 0):
                print(f'\nAn income of ${(income)} is in the top {round(float((get_percent(data, float(income)))[1]),2)}% of incomes.')
            else:
                print("Error: income must be positve")
        elif (choice == null):
            break
        else:
            print("Error in selection.")
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    

if __name__ == "__main__":
    main()