
from operator import index


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
    reviews = [[] for _ in range(N+1)]
    lines = fp.readlines()
    for line in lines:
        cur = line.split('\t')[0:3]
        reviews[int(cur[0])].append((int(cur[1]), int(cur[2])))
        reviews[int(cur[0])].sort()
    
    return reviews

def read_users(fp):
    ''' returns a list of tuples of age, gender, occupation'''
    users = [[]]
    lines = fp.readlines()
    for line in lines:
        cur = line.split('|')[1:4]
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
            pass
    return movies

def genre_movies(genre,L_movies):
    ''' Docstring'''
    pass   # remove this line

def gen_users (gender, L_users, L_reviews):
    ''' Docstring'''
    pass   # remove this line
          
def occ_users (occupation, L_users, L_reviews):
    ''' Docstring'''
    pass   # remove this line

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    pass   # remove this line
             
def highest_rated_by_reviewer(L_in,N_movies):
    ''' Docstring'''
    pass   # remove this line
 
def main():
    file = open_file('movies')
    L_movies = read_movies(file)
    year_movies(1940, L_movies)

if __name__ == "__main__":
    main()
                                           
