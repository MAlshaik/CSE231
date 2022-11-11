
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    '''This function prompts the user to input a file name to open and keeps prompting until a correct name is entered. '''
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
    '''This function reads the Names.txt file using file pointer, fp.'''
    lines = fp.readlines()
    names = []
    for line in lines:
        names.append(line.strip())
    
    return names


def read_friends(fp,names_lst):
    '''This function reads the Friends.csv file using file pointer, fp. '''
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
    '''This function takes the two lists created in the read_names function and the read_friends function and builds a dictionary.'''
    friends_dict = {}
    for name in names_lst:
        friends_dict[name] = friends_lst[names_lst.index(name)]
    
    return friends_dict
            
def find_common_friends(name1, name2, friends_dict):
    '''This function takes two names (strings) and the friends_dict (returned by the create_friends_dict) and returns a set of friends that the two names have in common. '''
    return set(friends_dict[name1]) & set(friends_dict[name2])

def find_max_friends(names_lst, friends_lst):
    '''This function takes a list of names and the corresponding list of friends and determines who has the most friends.'''
    len_friends = [len(x) for x in friends_lst]
    max_freinds = max(len_friends)
    max_names = [names_lst[i] for i in range(len(friends_lst)) if len(friends_lst[i]) == max_freinds]

    return sorted(max_names),max_freinds
    
    
def find_max_common_friends(friends_dict):
    '''This function takes the friends dictionary and finds which pairs of people have the most friends in common. '''
    max_common_friends = -9999
    pair = []
    pair_friends = []
    for key in friends_dict:
        for sec in friends_dict:
            if sec != key and (sec,key) not in pair:
                pair.append((key,sec))
                pair_friends.append(len(set(friends_dict[key]) & set(friends_dict[sec])))
    
    max_f = max(pair_friends)
    max_pair = [pair[i] for i in range(len(pair)) if pair_friends[i] == max_f]

    return max_pair, max_f
    
def find_second_friends(friends_dict):
    '''Find the freinds of freinds of each person in the dictionary'''
    second_dict = {}
    for key in friends_dict:
        second_dict[key] = set()
        base = {key}
        for i in friends_dict[key]:
            base.add(i)
            for n in friends_dict[i]:
                second_dict[key].add(n)
        second_dict[key] -= base
    
    return second_dict
        
        

def find_max_second_friends(seconds_dict):
    '''Find who has the most freinds of freinds'''
    m = list(seconds_dict.values())
    m_len = [len(i) for i in m]
    max_l = max(m_len)

    max_f = [i for i in list(seconds_dict.keys()) if len(seconds_dict[i]) == max_l]
    return max_f,max_l

def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)


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
            name = input("\nEnter a name: ")
            while True:
                try:
                    name_lst = friends_dict[name.strip()]
                    print(f"\nFriends of {name}:")
                    for i in name_lst:
                        print(i)
                    break

                except:
                    print(f"\nThe name {name} is not in the list.")
                    name = input("\nEnter a name: ")


        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
