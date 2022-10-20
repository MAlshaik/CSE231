


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word = input("Enter a word ('quit' to quit): \n")


while(word != 'quit'):
    word = word.lower()
    for i in VOWELS:
        if(word[0] == i):
            word += 'way'


    i = 0
    j=0
    con = False
    while(i < len(word)):
        if(j >= len(CONSONANTS)-1):
                break
        while(j<len(CONSONANTS)):
            if(j >= len(CONSONANTS)-1):
                if(con):
                    word = word + 'ay'
            if(word[i] == CONSONANTS[j]):
                con = True
                word += word[i]
                word = word[i+1:]
                j = 0
                i = 0
                
                    
            else:
                j+=1
        i += 1
                   
                
                
            
               
    
    print(word)

        
            

    word = input("Enter a word ('quit' to quit): \n")


        
# Error message used in Mimir test
#print("Can't convert empty string.  Try again.")
    