
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    '''Docstring'''
    file = input(f"\nInput a {s} file: ")
    while(True):
        try:
            data = open(file)
            break
        except:
             print("\nError in opening file.")
             file = input(f"\nInput a {s} file: ") 
             #makes sure the file is valid
    return data

def read_names(fp):
    '''Docstring'''
    lines = fp.readlines()
    names = []
    for line in lines:
        names.append(line.strip())
    
    return names


def read_friends(fp,names_lst):
    '''Docstring'''
    lines = fp.readlines()
    friends_list = []
    for line in lines:
        line = line.strip().split(',')
        line.pop()
        friends = []
        for index in line:
            friends.append(names_lst[int(index)])
        friends_list.append(friends)
    return friends_list
            

def create_friends_dict(names_lst,friends_lst):
    '''Docstring'''
    friends_dict = {}
    for name in names_lst:
        friends_dict[name] = friends_lst[names_lst.index(name)]
    
    return friends_dict
            
def find_common_friends(name1, name2, friends_dict):
    '''Docstring'''
    return set(friends_dict[name1]) & set(friends_dict[name2])

def find_max_friends(names_lst, friends_lst):
    '''Docstring'''
    len_friends = [len(x) for x in friends_lst]
    max_freinds = max(len_friends)
    max_names = [names_lst[i] for i in range(len(friends_lst)) if len(friends_lst[i]) == max]

    return max_names,max_freinds
    
    
def find_max_common_friends(friends_dict):
    '''Docstring'''
    
    
def find_second_friends(friends_dict):
    '''Docstring'''
    pass # replace with your code

def find_max_second_friends(seconds_dict):
    '''Docstring'''
    pass # replace with your code

def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    print("\nFriend Network:")
    for name,friends in friends_dict.items():
        print(name,":")
        print("   {}".format(friends))

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4":
            pass  # YOUR CODE GOES HERE

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()