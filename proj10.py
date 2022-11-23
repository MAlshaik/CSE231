
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    stock = Deck()
    foundations = [[] for i in range(4)]
    tableau = [[] for i in range(7)]
    for j in range(7):
        for i in range(j,7):
            tableau[i].append(stock.deal())
            if j != i:
                tableau[i][-1].flip_card()
    waste = [stock.deal()]
    return tableau, stock, foundations, waste

    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''Docstring'''
    if stock.is_empty():
        return False
    waste.append(stock.deal())
    return True
    
       
def waste_to_tableau( waste, tableau, t_num ):
    '''Docstring'''
    if len(waste) == 0:
        return False
    
    if len(tableau[t_num]) == 0:
        if waste[-1].rank() == 13:
            tableau[t_num].append(waste.pop())
            return True
        return False

    if waste[-1].suit() in (3,2) and tableau[t_num][-1].suit() in (1,4):
        if waste[-1].rank() + 1 == tableau[t_num][-1].rank():
            tableau[t_num].append(waste.pop())
            return True
        return False
    
    if waste[-1].suit() in (1,4) and tableau[t_num][-1].suit() in (3,2):
        if waste[-1].rank() + 1 == tableau[t_num][-1].rank():
            tableau[t_num].append(waste.pop())
            return True
        return False
    
    return False

def waste_to_foundation( waste, foundation, f_num ):
    '''Docstring'''
    if len(waste) == 0:
        return False

    if len(foundation[f_num]) == 0:
        if waste[-1].value() == 1:
            foundation[f_num].append(waste.pop())
            return True
        return False
    
    if waste[-1].suit() == foundation[f_num][-1].suit() and (waste[-1].rank() - 1) == foundation[f_num][-1].rank():
        foundation[f_num].append(waste.pop())
        return True

    return False


def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''Docstring'''
    if len(tableau[t_num]) == 0:
        return False

    if len(foundation[f_num]) == 0:
        if tableau[t_num][-1].value() == 1:
            foundation[f_num].append(tableau[t_num].pop())
            return True
        return False
    
    if tableau[t_num][-1].suit() == foundation[f_num][-1].suit() and (tableau[t_num][-1].rank() - 1) == foundation[f_num][-1].rank():
        foundation[f_num].append(tableau[t_num].pop())
        return True

    return False

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''Docstring'''
    if len(tableau[t_num1]) == 0:
        return False
    
    if len(tableau[t_num2]) == 0:
        if tableau[t_num1][-1].rank() == 13:
            tableau[t_num2].append(tableau[t_num1].pop())
            tableau[t_num1][-1].flip_card()
            return True
        return False

    if tableau[t_num1][-1].suit() in (3,2) and tableau[t_num2][-1].suit() in (1,4):
        if tableau[t_num1][-1].rank() + 1 == tableau[t_num2][-1].rank():
            tableau[t_num2].append(tableau[t_num1].pop())
            tableau[t_num2][-2].flip_card()
            try:
                tableau[t_num1][-1].flip_card()
            except:
                pass
            return True
        return False
    
    if tableau[t_num1][-1].suit() in (1,4) and tableau[t_num2][-1].suit() in (3,2):
        if tableau[t_num1][-1].rank() + 1 == tableau[t_num2][-1].rank():
            tableau[t_num2].append(tableau[t_num1].pop())
            tableau[t_num2][-2].flip_card()
            try:
                tableau[t_num1][-1].flip_card()
            except:
                pass
            return True
        return False
    
    return False
    
def check_win (stock, waste, foundation, tableau):
    '''Docstring'''
    if stock.is_empty() and len(waste) == 0:
        for i in tableau:
            if len(i) != 0:
                return False
        return True
    return False

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    tableau, stock, foundations, waste = initialize()
    print(MENU)
    
    option = ''
    while option != None:
        display(tableau, stock, foundations, waste)
        option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
        option = parse_option(option)
        while option == None:
            option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
            option = parse_option(option)

        if option[0] == "TT":
            valid = tableau_to_tableau(tableau, option[1]-1, option[2]-1)
            if valid:
                display(tableau, stock, foundations, waste)
            else:
                print("\nInvalid move!\n")
        elif option[0] == "TF":
            valid = tableau_to_foundation(tableau, foundations, option[1]-1, option[2]-1)
            if valid:
                if check_win(tableau, stock, foundations, waste):
                    print("You won!")
                    display(tableau, stock, foundations, waste)
                    quit()
            else:
                print("\nInvalid move!\n")
        elif option[0] == "w":
            if option[1] == 'f':
                valid = waste_to_foundation(waste, foundations, int(option[3]))
                if valid:
                    if check_win(tableau, stock, foundations, waste):
                        print("You won!")
                        display(tableau, stock, foundations, waste)
                        quit()
                else:
                    print("\nInvalid move!\n")
            else:
                if option[1] == 't':
                    valid = waste_to_tableau(waste, tableau, int(option[3]))
                    if valid:
                        display(tableau, stock, foundations, waste)
                    else:
                        print("\nInvalid move!\n")
        elif option == 'sw':
            valid = stock_to_waste()
            if valid:
                display(tableau, stock, foundations, waste)
            else:
                print("\nInvalid move!\n")
        elif option == 'r':
            stock.shuffle()
            tableau, stock, foundations, waste = initialize()
            print(MENU)
            display(tableau, stock, foundations, waste)
        elif option == 'h':
            print(MENU)
        elif option == 'q':
            quit()


if __name__ == '__main__':
     main()
