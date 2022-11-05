
import string
from operator import itemgetter


def add_word( word_map, word ):

    # YOUR COMMENT
    word = word.lower()
    word = word.capitalize()
    if word not in word_map:
        word_map[ word ] = 0

    # YOUR COMMENT
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # YOUR COMMENT
        word_list = line.split()

        for word in word_list:

            # YOUR COMMENT
            word = word.strip().strip(string.punctuation)
            if word != '':
                add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    # YOUR COMMENT
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # YOUR COMMENT
    freq_list = sorted( sorted(word_list), key=itemgetter(1), reverse=True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    
    try:
        in_file = open(input("Enter file name: "))
        print() #keep it for testing purposes in Coding Rooms
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = open(input("Enter file name: "))

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()
