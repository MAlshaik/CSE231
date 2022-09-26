###########################################################
#
#   Computer Project #4
#   Algorithm
#       prompt for an integer
#       input an integer
#       loop while not end-of-data
#       call function to count number of digits in integer
#       output the number of digits
#       prompt for an integer
#       input an integer
#    display closing message
#############################################################



def factorial(n):
    n = int(n)
    if(n < 0):
        return None 
    while n >= 1:
        fact =n* (n-1)
        n-=1
    return fact

def e():
    EPSILON = 0.0000001
    n = 1
    e = 1
    while(1/n > EPSILON):
        e += 1/(n*(n+1))
        n+=1

    return round(e,10)

def pi():
    n = 0
    pi = 0
    sig = (-1)**n/(2(n)+1)
    
    while (sig > EPSILON):
        sig = (-1)**n/(2(n)+1)
        pi += sig

    return round((pi*4),10)

def sinh(x):
    n = 0
    sig = (x**((2*n)+1))/(factorial(2*n+1))
    while(sig > EPSILON):
        sig = (x**((2*n)+1))/(factorial(2*n+1))
        n+=1 



        
