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
    if(n<=1 and n>=0):
        return 1

    if(n < 0):
        return None 

    fact = n*(n-1)
    n-=1
     
    while n > 1:
        fact *= (n-1)
        n-=1
    return fact

def e():
    n = 1
    e = 1
    while(1/factorial(n) >= EPSILON):
        e += 1/factorial(n)
        n+=1

    return round(e,10)

def pi():
    n = 0
    pi = 0
    sig = (-1)**n/((2*n)+1)
    
    while (math.fabs(sig) > EPSILON):
        sig = (-1)**n/((2*n)+1)
        if math.fabs(sig) > EPSILON:
            pi += sig
        n+=1

    return round(pi*4,10)

def sinh(x):
    n = 0
    sig = (x**((2*n)+1))/(factorial(2*n+1))
    sinh = 0
    while(sig > EPSILON):
        sig = (x**((2*n)+1))/(factorial(2*n+1))
        if math.fabs(sig) > EPSILON:
            sinh += sig
        n+=1
    return round(sinh,10)

def main():
    print(MENU)
    func = ''

    while(func != 'x'):
        func = input("\nChoose an option: \n").lower()
        if(func == 'f'):
            print('Factorial\n')
            N = int(input('Input non-negative integer N: \n'))

            calc = factorial(N)
            mth = math.factorial(N)
            diff = calc-mth

            print(f'Calculated: {calc}')
            print(f'Math: {mth}')
            print(f'Diff: {diff}')

            continue
        if(func == 'e'):
            
            print('e')

            calc = e()
            mth = math.e
            diff = math.fabs(calc-mth)

            print(f'Calculated: {calc:.10f}')
            print(f'Math: {mth:.10f}')
            print(f'Diff: {diff:.10f}')

            

        if(func == 'p'):
            print('pi')

            calc = pi()
            mth = math.pi
            diff = math.fabs(calc-mth)

            print(f'Calculated: {calc:.10f}')
            print(f'Math: {mth:.10f}')
            print(f'Diff: {diff:.10f}')

            

        if(func == 's'):
            print('sinh\n')
            x = float(input('X in radians: '))

            calc = sinh(x)
            mth = math.sinh(x)
            diff = math.fabs(calc-mth)

            print(f'Calculated: {calc:.10f}')
            print(f'Math: {mth:.10f}')
            print(f'Diff: {diff:.10f}')

            
        if(func == 'm'):
            print(MENU)
    
    print("Thank you for playing.")
        
if __name__ == '__main__': 
    main()




        
