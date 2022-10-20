###########################################################
#
#   Computer Project #4
#   Algorithm
#       print menue of options
#       prompt for option
#       if the function requires input, prompt for input
#       run the function corrisponding to the option
#       output the result rounded to 10 decimal places
#       ask for another option
#       if option is x then exit and display the closing message
#############################################################

import math
EPSILON = 0.0000001 

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

def factorial(n):
    n = int(n)
    #transforms input to int
    if(n<=1 and n>=0):
        return 1
    #if n == 1 or 0 return 1

    if(n < 0):
        return None 
    #if n is negative return None 

    fact = n*(n-1)
    n-=1
     
    while n > 1:
        fact *= (n-1)
        n-=1
    return fact
    #calculate the factorial of n and returns it

def e():
    n = 1
    e = 1
    while(1/factorial(n) >= EPSILON):
        e += 1/factorial(n)
        #calls the factorial function to find the factorial of the denominator
        n+=1

    return round(e,10)
    #calculate e and return it

def pi():
    n = 0
    pi = 0
    sig = (-1)**n/((2*n)+1)
    
    while (math.fabs(sig) > EPSILON):
        sig = (-1)**n/((2*n)+1)
        if math.fabs(sig) > EPSILON:
            pi += sig
        #makes sure that sig is more than EPSILON before adding it to pi
        n+=1
    return round(pi*4,10)
    #return the value of pi rounded to 10 decimal places

def sinh(x):
    try:
        x = float(x)
        #makes sure that x is floatable
    except:
        return None
    n = 0
    sig = (x**((2*n)+1))/(factorial(2*n+1))
    sinh = 0
    while(math.fabs(sig) > EPSILON):
        sig = (x**((2*n)+1))/(factorial(2*n+1))
        if math.fabs(sig) > EPSILON:
            sinh += sig
        #makes sure sig is more than EPSILON before adding it to sinh
        n+=1
    return round(sinh,10)
    #returns the sinh value rounded to 10 decimal places
def main():
    print(MENU)
    func = ''

    while(func != 'x'):
        func = input("\nChoose an option: \n").lower()
        if(func == 'f'):
            print('Factorial')
            try:
                N = int(input('Input non-negative integer N: \n'))
                if(N<0):
                    print("Invalid N.")
                    continue 
            #makes sure that N is a valid, positive integer
            except:
                print("Invalid N.")
                continue  
            

            calc = factorial(N)
            mth = math.factorial(N)
            diff = calc-mth

            print(f'Calculated: {calc}')
            print(f'Math: {mth}')
            print(f'Diff: {diff}')
            #prints the result
            
        elif(func == 'e'):
            
            print('e')

            calc = e()
            mth = math.e
            diff = math.fabs(calc-mth)

            print(f'Calculated: {calc:.10f}')
            print(f'Math: {mth:.10f}')
            print(f'Diff: {diff:.10f}')
            #prints the result

        elif(func == 'p'):
            print('pi')

            calc = pi()
            mth = math.pi
            diff = math.fabs(calc-mth)

            print(f'Calculated: {calc:.10f}')
            print(f'Math: {mth:.10f}')
            print(f'Diff: {diff:.10f}')
            #prints the result

            

        elif(func == 's'):
            print('sinh')
            try:
                x = float(input('X in radians: \n'))
            except:
                print("Invalid X.")
                continue

            calc = sinh(x)
            mth = math.sinh(x)
            diff = math.fabs(calc-mth)

            print(f'Calculated: {calc:.10f}')
            print(f'Math: {mth:.10f}')
            print(f'Diff: {diff:.10f}')
            #prints the result

            
        elif(func == 'm'):
            print('''Options below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
''')

        elif(func != 'x'):
            print(f"Invalid option: {func.upper()}")
            print(MENU)
        
    print("Thank you for playing.")
        
if __name__ == '__main__': 
    main()




        
