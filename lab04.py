import enum

from pyrsistent import v
from sqlalchemy import false

#PART B 

def leap_year(year): 
    return (int(year) % 400 == 0) or ((int(year) % 4 == 0) and (int(year) % 100 != 0))
    

print(leap_year('1896'))
print(leap_year('1904'))
print(leap_year('2000'))
print(leap_year('1900'))


#PART C
def digit_count(number):
    number = str(int(number))
    even = 0
    odd = 0
    zero = 0
    for i,n in enumerate(number):
        
        if(int(n) == 0):
            zero += 1
        elif (int(n) % 2 == 0):
            even += 1
        else: 
            odd += 1
    return [even, odd, zero]


print(digit_count(1234567890123))
print(digit_count(123400.345))
print(digit_count(123.))
print(digit_count(0.123))

#PART D

def rotate(s,n):
    return s[len(s)-n:] + s[: len(s)-n]

print(rotate('abcdefgh',3))




#PART E 

def float_check(number):

    if(number.count('.') > 1):
        return False
    else:
        number = number.replace('.', '')
    
    for i,n in enumerate(number):
        if(n.isdigit() == False):
            return False
    return True
  

print(float_check('1234'))
print(float_check('123.45'))
print(float_check('123.45.67'))
print(float_check('34e46'))
print(float_check('.45'))
print(float_check('45.'))
print(float_check('45..'))
