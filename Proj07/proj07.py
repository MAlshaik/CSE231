###########################################################
#
#   Computer Project #7
#   Algorithm
#       Define all methods needed    
#       prompt for users, reviews, and movie files until valid values are entered
#       print menue
#       prompt user for option 1-5
#       depending on option, call required functions
#       ask for user for input if needed
#       print results
#       Ask for user input again until input is 5
#############################################################


GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s):
    '''This function prompts the user to input a file name to open and keeps prompting until a
correct name is entered.'''
    file = input(f'\nInput {s} filename: ')
    while(True):
        try:
            data = open(file)
            break
        except:
             print('\nError: No such file; please try again.')
             file = input(f'\nInput {s} filename: ') 
             #makes sure the csv file is valid
    return data
    
def read_reviews(N,fp):
    ''' returns a list of tuple of the movie id and raiting'''
    reviews = [[] for x in range(N+1)]
    # initilizes list of size N+1
    lines = fp.readlines()
    for line in lines:
        cur = line.split('\t')[0:3]
        #splits the text file everywhere there is a tab and omits last value
        reviews[int(cur[0])].append((int(cur[1]), int(cur[2])))
        reviews[int(cur[0])].sort()
    
    return reviews

def read_users(fp):
    ''' returns a list of tuples of age, gender, occupation'''
    users = [[]]
    lines = fp.readlines()
    for line in lines:
        cur = line.split('|')[1:4]
        #splits the user text file everywhere there is a |
        cur[0] = int(cur[0])
        users.append(tuple(cur))
    return users
    

def read_movies(fp):
    ''' returns a list of tuples which contain the title, date, and the list of genre'''
    movies = [[]]
    lines = fp.readlines()
    for line in lines:
        cur_genre = line.split('|')[5:]
        genre = []
        for i in range(len(cur_genre)):
            if int(cur_genre[i]) == 1:
                # if the genre is true, then it appends that genre's title to the list of genres
                genre.append(GENRES[i])
        cur = line.split('|')[1:3]
        cur.append(genre)
        movies.append(tuple(cur))
    return movies

        
def year_movies(year,L_movies):
    ''' This function filters for movies in a specific year and returns their ids 
    movieID (ints) as a sorted list in ascending order'''
    movies = []
    for movie in L_movies:
        try:
            date = int(movie[1][-4:])
            if date == year:
                movies.append(L_movies.index(movie))
        except:
            # try an except is used in case the list date is being indexed into is empty
            pass
    return movies

def genre_movies(genre,L_movies):
    ''' This function filters the main movie list to find movies for a specific genre and returns their ids as a list.'''
    movies = []
    for tup in L_movies:
        try:
            for gen in tup[2]:
                if gen.lower() == genre.lower():
                    #made sure both gen and genre are lower case so no errors are in user input
                    movies.append(L_movies.index(tup))
        except:
            pass
    return movies

def gen_users (gender, L_users, L_reviews):
    ''' This function filters the main reviews list to find reviews for a specific gender of users and returns them as a list of lists.'''
    gen_mov = []
    for i in range(len(L_users)):
        try:
            if L_users[i][1].lower() == gender.lower():
                gen_mov.append(L_reviews[i])
        except:
            pass
    return gen_mov

          
def occ_users (occupation, L_users, L_reviews):
    ''' This function filters the main reviews list to find records for a specific occupational group of users and returns them as a list of lists of 
    tuples.'''
    occ_use = []
    for i in range(len(L_users)):
        try:
            if L_users[i][2].lower() == occupation.lower():
                occ_use.append(L_reviews[i])
        except:
            pass
    return occ_use

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' This function calculates the average rating for the reviews in L_reviews list of the movies in L_in list and returns a list of the highest
     average rated movies and the highest average. '''
    avg = [0 for x in range(N_movies+1)] 
    for i in range(len(avg)):
        if i in L_in:
            raiting = 0
            rep = 0
            for list in L_reviews:
                for tup in list:
                    if tup[0] == i:
                    #adds one to the repitition of the raiting for that movie and adds the raiting to the total raiting of the movie
                        rep += 1
                        raiting += tup[1]
            try:
                avg[i] = raiting/rep
                #appends the average raiting to the avg list
            except:
                avg[i] = 0
    index = [j for j in range(len(avg)) if round(avg[j],2) == round(max(avg),2)]
    return index, round(max(avg),2)
             
def highest_rated_by_reviewer(L_in,N_movies):
    ''' This function calculates the average rating for movies by a specific group of users (L_in) and returns a list of the highest average rated movies and the highest average.'''
    avg = [0 for x in range(N_movies+1)] 
    for i in range(len(avg)):
            raiting = 0
            rep = 0
            for list in L_in:
                for tup in list:
                    if tup[0] == i:
                        rep += 1
                        raiting += tup[1]
            try:
                avg[i] = raiting/rep
            except:
                avg[i] = 0
   
    index = [j for j in range(len(avg)) if avg[j] == max(avg)]
    return index, round(max(avg),2)
 
def main():
    file = open_file('users')
    L_users = read_users(file)
    file = open_file('reviews')
    L_reviews = read_reviews(100000,file)
    file = open_file('movies')
    L_movies = read_movies(file)

    option = 0
    print(MENU)
    while option != 5:
        option = int(input('\nSelect an option (1-5): '))
        while option not in range(1,6):
            print("\nError: not a valid option.")
            option = int(input('\nSelect an option (1-5): '))

        if option == 1:
            year = int(input('\nInput a year: '))
            while year < 1930 or year > 1998:
                print("\nError in year.")
                year = int(input('\nInput a year: '))
            
            year_mov = year_movies(year, L_movies)
            id, avg = highest_rated_by_movie(year_mov, L_reviews, len(L_movies))

            print(f'\nAvg max rating for the year is: {avg}')
            for i in id:
            #goes through each integer in id and prints the corrispoding movie name
                print(L_movies[i][0])

        if option == 2:
            genres = [gen.lower() for gen in GENRES]
            print(f'\nValid Genres are:  {GENRES}')
            genre = input('Input a genre: ').lower()
            while genre not in genres:
                print("\nError in genre.")
                genre = input('Input a genre: ').lower()

            genre_mov = genre_movies(genre, L_movies)
            id, avg = highest_rated_by_movie(genre_mov, L_reviews, len(L_movies))

            print(f'\nAvg max rating for the Genre is: {avg}')
            for i in id:
                print(L_movies[i][0])

        if option == 3:
            gender = input('\nInput a gender (M,F): ').lower()
            while gender != 'm' and gender != 'f':
                print("\nError in gender.")
                gender = input('\nInput a gender (M,F): ').lower()
            
            gen_user = gen_users(gender.upper(), L_users, L_reviews)
            id, avg = highest_rated_by_reviewer(gen_user, len(L_movies))

            print(f'\nAvg max rating for the Gender is: {avg}')
            for i in id:
                print(L_movies[i][0])

        if option == 4:
            occupations = [ocu.lower() for ocu in OCCUPATIONS]
            print(f'\nValid Occupatipns are:  {OCCUPATIONS}')
            occupation = input('Input an occupation: ').lower()
            while occupation not in occupations:
                print("\nError in occupation.")
                occupation = input('Input an occupation: ').lower()

            occ_user = occ_users(occupation, L_users, L_reviews)
            id, avg = highest_rated_by_reviewer(occ_user, len(L_movies))

            print(f'\nAvg max rating for the occupation is: {avg}')
            for i in id:
                print(L_movies[i][0])


if __name__ == "__main__":
    main()
                                           
