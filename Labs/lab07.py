
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    reader = csv.reader(fp) # attaches a reader to the file fp
    
   
    next(reader,None) 
    next(reader,None) 
    next(reader,None) 
    next(reader,None)
    next(reader,None)
    next(reader,None) 

    lineList = []
    for line in reader: # line is a list
        edited_list = list(filter(None, line))
        lineList.append(edited_list)
    lineList = list(filter(None, lineList))
    return lineList  # temoprary return value so main runs

def get_totals(L):
    total_pop = 0
    us_pop = float(L[0][1].replace(',', ''))
    for i in range(len(L)-1):
        i += 1
        num = L[i][1].replace(',', '')
        num = num.replace('<', '')
        total_pop += float(num)

    return us_pop,total_pop  # temoprary return value so main runs

def get_industry_counts(L):
    cons_count = manu_count = lei_count = bus_count = agri_count = 0
    indus_count = []
    for list in L:
        if(list[9] == 'Construction'):
            cons_count += 1
        if(list[9] == 'Agriculture'):
            agri_count += 1
        if(list[9] == 'Manufacturing'):
            manu_count += 1
        if(list[9] == 'Leisure/hospitality'):
            lei_count += 1
        if(list[9] == 'Business services'):
            bus_count += 1
    
    indus_count.append(['Construction',cons_count])
    indus_count.append(['Manufacturing', manu_count]) 
    indus_count.append(['Leisure/hospitality', lei_count]) 
    indus_count.append(['Business services', bus_count])
    indus_count.append(['Agriculture', agri_count])
    return indus_count

def get_largest_states(L):
    state_list = []
    us_percent = float(L[0][2].replace('%', ''))
    for i in range(len(L)-1):
        i += 1
        num = float(L[i][2].replace('%', ''))
        if(num > us_percent):
            state_list.append(L[i][0])
    return state_list 

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)

    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()